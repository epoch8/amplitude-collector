import logging

from starlette import status
from starlette.responses import Response

from src.amplitude import AmplitudeRequestProcessor, RequestContentTypeError
from src.config import DEBUG, KAFKA_TOPIC
from src.kafka_producer import kafka_producer

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
            print(request.headers)
        return Response("success")
    except RequestContentTypeError as e:
        logger.error(str(e))
        return Response(
            "unexpected content type", status_code=status.HTTP_400_BAD_REQUEST
        )
