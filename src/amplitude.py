import json
import uuid
from datetime import datetime

from kafka.producer import KafkaProducer
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
            separate_records = await self._convert_form_data_to_json()
        elif self.content_type.startswith("application/json"):
            separate_records = await self._convert_dict_to_json()
        else:
            raise RequestContentTypeError(
                f"unexpected content type: {self.content_type}"
            )
        for record in separate_records:
            self.producer.send(
                topic=self.topic,
                value=json.dumps(record).encode("utf-8"),
                key=record["ingest_uuid"].encode("utf-8"),
            )
        self.producer.flush()
        return separate_records

    async def _convert_form_data_to_json(self):
        data = dict((await self.request.form())._dict)
        separate_records = await self._prepare_separate_records(data)
        return separate_records

    async def _convert_dict_to_json(self):
        data = await self.request.json()
        separate_records = await self._prepare_separate_records(data)
        return separate_records

    
    async def _prepare_separate_records(self, record: dict) -> list:
        record["ip_address"] = self.request.client.host
        record["collector_upload_time"] = datetime.now().isoformat()
        events = json.loads(record["e"])
        result = []
        for event in events:
            separate_data = record.copy()
            separate_data["ingest_uuid"] = uuid.uuid4().hex
            separate_data["e"] = json.dumps(event)
            result.append(separate_data)
        return result
