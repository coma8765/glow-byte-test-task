"""Application


"""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core import add_fastapi_prometheus, configure_logging, get_api_config
from src.modules.api.routes import router

config = get_api_config()
configure_logging(config.log_level)


@asynccontextmanager
async def bootstrap_app(_: FastAPI):
    yield


app = FastAPI(lifespan=bootstrap_app)
add_fastapi_prometheus(app)
app.include_router(router)
