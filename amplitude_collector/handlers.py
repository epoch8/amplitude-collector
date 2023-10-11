import datetime
import logging
from typing import Dict, Iterator, List
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


def _prepare_separate_records(request: Request, record: dict) -> Iterator[Dict]:
    events = orjson.loads(record["e"])
    del record["e"]

    if "x-real-ip" in request.headers:
        ip_address = request.headers["x-real-ip"]
    else:
        ip_address = request.client.host

    collector_upload_time = datetime.datetime.now().isoformat()

    for event in events:
        event["ip_address"] = ip_address
        event["collector_upload_time"] = collector_upload_time

        separate_data = record.copy()
        separate_data["ingest_uuid"] = uuid7str()
        separate_data["e"] = event

        yield separate_data


async def collect(request: Request) -> Response:
    content_type = request.headers.get("content-type", "")

    if content_type.startswith("application/x-www-form-urlencoded"):
        separate_records = _prepare_separate_records(
            request=request,
            record=dict((await request.form())._dict),
        )
    elif content_type.startswith("application/json"):
        separate_records = _prepare_separate_records(
            request=request,
            record=orjson.loads(await request.body()),
        )
    else:
        return Response(
            f"Unexpected content type: {content_type}",
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
