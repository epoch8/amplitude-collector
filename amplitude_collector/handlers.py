import datetime
import logging
from typing import Dict, List
import orjson

from starlette import status
from starlette.requests import Request
from starlette.responses import Response
from uuid_extensions import uuid7str

from .config import DEBUG, KAFKA_TOPIC
from .kafka_producer import kafka_producer

logger = logging.getLogger(__name__)


async def index(request):
    return Response("ok")


def _convert_form_data_to_json(request, form_dict: Dict) -> List[Dict]:
    separate_records = _prepare_separate_records(request, form_dict)
    return separate_records


def _convert_dict_to_json(request, body_bytes: bytes) -> List[Dict]:
    data = orjson.loads(body_bytes)
    separate_records = _prepare_separate_records(request, data)
    return separate_records


def _prepare_separate_records(request, record: dict) -> List[Dict]:
    events = orjson.loads(record["e"])
    del record["e"]

    if "x-real-ip" in request.headers:
        ip_address = request.headers["x-real-ip"]
    else:
        ip_address = request.client.host

    collector_upload_time = datetime.datetime.now().isoformat()

    result = []
    for event in events:
        event["ip_address"] = ip_address
        event["collector_upload_time"] = collector_upload_time

        separate_data = record.copy()
        separate_data["ingest_uuid"] = uuid7str()
        separate_data["e"] = orjson.dumps(event).decode("utf-8")
        result.append(separate_data)
    return result


async def collect(request: Request) -> Response:
    content_type = request.headers.get("content-type", "")

    if content_type.startswith("application/x-www-form-urlencoded"):
        separate_records = _convert_form_data_to_json(
            request=request,
            form_dict=dict((await request.form())._dict),
        )
    elif content_type.startswith("application/json"):
        separate_records = _convert_dict_to_json(
            request=request,
            body_bytes=await request.body(),
        )
    else:
        return Response(
            f"unexpected content type: {content_type}",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    for record in separate_records:
        kafka_producer.send(
            topic=KAFKA_TOPIC,
            value=orjson.dumps(record),
            key=record["ingest_uuid"].encode("utf-8"),
        )

    kafka_producer.flush()

    # send_data = await AmplitudeRequestProcessor(
    #     request=request, producer=kafka_producer, topic=KAFKA_TOPIC
    # ).execute()
    if DEBUG:
        print(separate_records)
        print(request.headers)

    return Response("success")
