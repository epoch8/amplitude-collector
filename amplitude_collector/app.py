import contextlib
from typing import AsyncIterator
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route
from starlette_exporter import PrometheusMiddleware, handle_metrics

from .handlers import collect, index
from .kafka_producer import make_kafka_producer


@contextlib.asynccontextmanager
async def lifespan(app: Starlette) -> AsyncIterator[dict]:
    kafka_producer = await make_kafka_producer()

    yield {"kafka_producer": kafka_producer}

    await kafka_producer.stop()


app = Starlette(
    debug=True,
    routes=[
        Route("/", index, methods=["GET"]),
        Route("/collect", collect, methods=["POST", "GET"]),
        Route("/metrics", handle_metrics),
    ],
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(
            PrometheusMiddleware,
            app_name="collector",
        ),
    ],
    lifespan=lifespan,
)
