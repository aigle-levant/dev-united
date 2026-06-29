"""
what is this: routes for monitoring

route features:
- GET /health: This returns health metrics
"""

# imports
from fastapi import APIRouter

health_router = APIRouter(prefix="/health", tags=["Health"])

@health_router.get("/health")
async def fetch_profile(status):
    return {
        "status": "ok"
    }