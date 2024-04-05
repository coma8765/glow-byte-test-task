"""Application logging

Typical usage example:

    _logger: Logger = get_logger("module-name")
"""
from logging import Logger, basicConfig, getLogger
from typing import Literal

_app_logger = getLogger("app")

LoggingLevelType = Literal[
    "CRITICAL",
    "FATAL",
    "ERROR",
    "WARN",
    "WARNING",
    "INFO",
    "DEBUG",
]


def get_logger(name: str | None = None) -> Logger:
    """Returns logger

    :param name: (Optional) name of logger
    :return: if name is None return global logger else return module logger
    """
    if name:
        return _app_logger.getChild(name)
    return _app_logger


def configure_logging(level: int | LoggingLevelType = "INFO"):
    basicConfig(level=level)


__all__ = [
    "get_logger",
    "configure_logging",
    "LoggingLevelType",
]
