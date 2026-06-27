from pydantic import BaseModel
from typing import Optional

class ResolveRequest(BaseModel):
    name: str
    github: Optional[str] = None
    stackoverflow: Optional[str] = None
    devto: Optional[str] = None
    hackernews: Optional[str] = None
    email_hint: Optional[str] = None

class ResolveResponse(BaseModel):
    profile_id: str
    status: str

class HealthResponse(BaseModel):
    status: str
    github_remaining: int
    github_limit: int
    profiles_resolved: int