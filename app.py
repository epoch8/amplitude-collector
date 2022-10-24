import os
import logging

from kafka import KafkaProducer
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response
from starlette.routing import Route

from amplitude import AmplitudeRequestProcessor, RequestContentTypeError

logger = logging.getLogger(__name__)

KAFKA_DSN = os.environ["KAFKA_DSN"]
# KAFKA_USE_SSL = os.environ.get("KAFKA_USE_SSL")
KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "events")

KAFKA_USERNAME = os.environ.get("KAFKA_USERNAME", "collector")
KAFKA_PASSWORD = os.environ.get("KAFKA_PASSWORD", "")

DEBUG = os.environ.get("DEBUG", "True") == "True"


kafka_producer = KafkaProducer(
    bootstrap_servers=KAFKA_DSN,
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-512",
    sasl_plain_password=KAFKA_PASSWORD,
    sasl_plain_username=KAFKA_USERNAME,
    ssl_cafile="cert/Yandex/CA.pem",
)


async def index(request):
    return Response("ok")


async def collect(request):
    try:
        send_data = AmplitudeRequestProcessor(
            request=request, producer=kafka_producer, topic=KAFKA_TOPIC
        ).execute()
        if DEBUG:
            print(send_data)
    except RequestContentTypeError as e:
        logger.error(str(e))
    return Response("success")


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
