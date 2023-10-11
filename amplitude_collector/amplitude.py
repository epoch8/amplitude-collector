from typing import Dict, List
from uuid_extensions import uuid7str
from datetime import datetime

from kafka.producer import KafkaProducer
import orjson
from starlette.requests import Request


class RequestContentTypeError(ValueError):
    pass


class AmplitudeRequestProcessor:
    def __init__(self, request: Request, producer: KafkaProducer, topic: str):
        self.request = request
        self.producer = producer
        self.topic = topic

    @property
    def content_type(self) -> str:
        return self.request.headers.get("content-type", "")

    async def execute(self):
        if self.content_type.startswith("application/x-www-form-urlencoded"):
            separate_records = self._convert_form_data_to_json(
                dict((await self.request.form())._dict)
            )
        elif self.content_type.startswith("application/json"):
            separate_records = self._convert_dict_to_json(await self.request.body())
        else:
            raise RequestContentTypeError(
                f"unexpected content type: {self.content_type}"
            )
        for record in separate_records:
            self.producer.send(
                topic=self.topic,
                value=orjson.dumps(record),
                key=record["ingest_uuid"].encode("utf-8"),
            )
        self.producer.flush()
        return separate_records

    def _convert_form_data_to_json(self, form_dict: Dict) -> List[Dict]:
        separate_records = self._prepare_separate_records(form_dict)
        return separate_records

    def _convert_dict_to_json(self, body_bytes: bytes) -> List[Dict]:
        data = orjson.loads(body_bytes)
        separate_records = self._prepare_separate_records(data)
        return separate_records

    def _prepare_separate_records(self, record: dict) -> List[Dict]:
        events = orjson.loads(record["e"])
        del record["e"]

        if "x-real-ip" in self.request.headers:
            ip_address = self.request.headers["x-real-ip"]
        else:
            ip_address = self.request.client.host

        collector_upload_time = datetime.now().isoformat()

        result = []
        for event in events:
            event["ip_address"] = ip_address
            event["collector_upload_time"] = collector_upload_time

            separate_data = record.copy()
            separate_data["ingest_uuid"] = uuid7str()
            separate_data["e"] = orjson.dumps(event).decode("utf-8")
            result.append(separate_data)
        return result
