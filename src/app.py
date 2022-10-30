import logging

from starlette import status
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response
from starlette.routing import Route

from src.amplitude import AmplitudeRequestProcessor, RequestContentTypeError
from src.config import DEBUG, KAFKA_TOPIC, kafka_producer

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
        return Response("success")
    except RequestContentTypeError as e:
        logger.error(str(e))
        return Response(
            "unexpected content type", status_code=status.HTTP_400_BAD_REQUEST
        )


app = Starlette(
    debug=True,
    routes=[
        Route("/", index, methods=["GET"]),
        Route("/collect", collect, methods=["POST", "GET"]),
    ],
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ],
)
