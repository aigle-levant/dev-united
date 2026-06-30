"""
what is this: routes for profile

route features:
- POST /profiles/resolve: This receives a search query, returns profile id
- GET /profiles/{id}: Fetches merged profile using data from various platforms
"""

# imports
from fastapi import APIRouter, HTTPException
from schemas.routes import ResolveRequest
from services.resolve_profile_service import resolve_profile_service as resolve_profile
from services.get_profile import get_profile
import time
from services.check_health import log_resolution

profile_router = APIRouter(prefix="/profiles", tags=["Profiles"])

@profile_router.post("/resolve")
async def resolve_profile_route(req: ResolveRequest):
    start_time = time.time()

    result = await resolve_profile(req)

    duration_ms = (time.time() - start_time) * 1000
    log_resolution(duration_ms)

    return result


@profile_router.get("/{profile_id}")
async def fetch_profile(profile_id: str):

    profile = get_profile(profile_id)

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found",
        )

    return profile
