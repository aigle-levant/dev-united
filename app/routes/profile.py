"""
what is this: routes for profile

route features:
- POST /profiles/resolve: This receives a search query, returns profile id
- GET /profiles/{id}: Fetches merged profile using data from various platforms
"""

# imports
from fastapi import APIRouter
from app.schemas.routes import ResolveRequest
from services.resolve_profile_service import resolve_profile_service as resolve_profile

profile_router = APIRouter(prefix="/profiles", tags=["Profiles"])

@profile_router.post("/profiles/resolve")
async def resolve_profile_route(req: ResolveRequest):
    profile_id = await resolve_profile(req)
    return { "profile-id": profile_id }

@profile_router.get("/{profile_id}")
async def fetch_profile(id: str):
    return {
        "id": id,
    }