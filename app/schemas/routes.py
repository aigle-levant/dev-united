from pydantic import BaseModel
from typing import Optional
from schemas.normalize import NormalizedAccount

class ResolveRequest(BaseModel):
    name: str
    github: Optional[str] = None
    stackoverflow: Optional[str] = None
    devto: Optional[str] = None
    hackernews: Optional[str] = None
    email_hint: Optional[str] = None

class ResolveResponse(BaseModel):
    profile_id: str

class HealthResponse(BaseModel):
    status: str

    github_remaining: int
    github_limit: int
    github_reset: int | None = None

    github_calls: int
    stackoverflow_calls: int
    devto_calls: int
    hackernews_calls: int

    llm_tokens: int
    estimated_cost: float

    profiles_resolved: int
    average_resolution_time_ms: float

class CanonicalProfile(BaseModel):
    name: str | None = None

    bio: str | None = None

    location: str | None = None

    website: str | None = None

    github: str | None = None

    twitter: str | None = None

    email: str | None = None

    summary: str | None = None

    languages: list[str] = []

    interests: list[str] = []

    reputation: int | None = None

class MatchResult(BaseModel):
    source: str
    confidence: int
    matched: bool
    account: NormalizedAccount

class ProfileResponse(BaseModel):
    profile_id: str

    canonical: CanonicalProfile

    matches: list[MatchResult]

    sources: dict[str, dict]

class ProfileLink(BaseModel):
    source: str
    external_id: str
    confidence: int