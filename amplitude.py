import json

from starlette.requests import Request
from kafka.producer import KafkaProducer


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

    def execute(self):
        if self.content_type == "application/x-www-form-urlencoded":
            data = self._convert_form_data_to_json()
        elif self.content_type == "application/json":
            data = await self.request.body()
        else:
            raise RequestContentTypeError(f"unexpected content type: {self.content_type}")

        self.producer.send(
            topic=self.topic,
            value=data,
            key=b"event"
        )
        self.producer.flush()
        return data

    async def _convert_form_data_to_json(self):
        form_data = await self.request.form()
        return json.dumps(form_data._dict).encode("utf-8")

