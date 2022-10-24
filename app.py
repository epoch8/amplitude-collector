import json
import os

from kafka import KafkaProducer
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response
from starlette.routing import Route

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
    ct = request.headers.get("content-type", "")
    if ct.startswith("application/x-www-form-urlencoded"):
        value = json.dumps((await request.form())._dict).encode("utf-8")

        kafka_producer.send(
            topic=KAFKA_TOPIC,
            value=value,
            key=b"event"
        )
        kafka_producer.flush()
        if DEBUG:
            print(value)

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
