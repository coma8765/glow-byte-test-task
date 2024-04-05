"""API Routes for first version of API"""
from fastapi import APIRouter

from src.modules.api.routes.v1 import reservations

router = APIRouter()

router.include_router(reservations.router, prefix="/reservation")

__all__ = ["router"]
