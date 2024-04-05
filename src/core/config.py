"""Application environment configuration provider

Copy `.env.example` to `.env` for pure usa
or to `.env.docker` for docker-based use.
Or setup environment variables use system methods.
"""
import logging
from dataclasses import dataclass
from functools import lru_cache

from environs import Env

from src.core.logging import LoggingLevelType


@dataclass
class APIConfig:
    log_level: int | LoggingLevelType = logging.INFO
    enable_metrics: bool = True


@lru_cache()
def get_api_config() -> APIConfig:
    env = Env()
    env.read_env()

    return APIConfig(
        log_level=env.log_level("LOG_LEVEL", APIConfig.log_level),
        enable_metrics=env.bool("ENABLE_METRICS", APIConfig.enable_metrics),
    )


__all__ = [
    "get_api_config",
    "APIConfig",
]
