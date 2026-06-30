"""
what is this: routes for profile

route features:
- POST /profiles/resolve: This receives a search query, returns profile id
- GET /profiles/{id}: Fetches merged profile using data from various platforms
"""

# imports
from fastapi import APIRouter
from schemas.routes import ResolveRequest
from services.resolve_profile_service import resolve_profile_service as resolve_profile
import time
from services.check_health import log_resolution

profile_router = APIRouter(prefix="/profiles", tags=["Profiles"])

@profile_router.post("/resolve")
async def resolve_profile_route(req: ResolveRequest):
    start_time = time.time()
    res = await resolve_profile(req)
    duration_ms = (time.time() - start_time) * 1000
    log_resolution(duration_ms)
    
    return res


@profile_router.get("/{profile_id}")
async def fetch_profile(profile_id: str):
    return {
        "profile_id": 100
    }
