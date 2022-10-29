from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route

from src.handlers import collect, index

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
