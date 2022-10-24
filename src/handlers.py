import logging

from starlette.responses import Response

from src.amplitude import AmplitudeRequestProcessor, RequestContentTypeError
from src.kafka_producer import kafka_producer
from src.config import KAFKA_TOPIC, DEBUG


logger = logging.getLogger(__name__)


async def index(request):
    return Response("ok")


async def collect(request):
    try:
        send_data = await AmplitudeRequestProcessor(
            request=request, producer=kafka_producer, topic=KAFKA_TOPIC
        ).execute()
        if DEBUG:
            print(send_data)
    except RequestContentTypeError as e:
        logger.error(str(e))
    return Response("success")
