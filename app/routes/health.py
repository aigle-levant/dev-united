"""
what is this: routes for monitoring

route features:
- GET /health: This returns health metrics
"""

# imports
from fastapi import APIRouter
from services.check_health import get_health_report

health_router = APIRouter(prefix="/health", tags=["Health"])

@health_router.get("/")
async def health():
    return get_health_report()