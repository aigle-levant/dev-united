from pydantic import BaseModel

class CanonicalProfile(BaseModel):
    id: str

    name: str | None
    location: str | None
    bio: str | None

    github_username: str | None
    stackoverflow_id: int | None
    devto_username: str | None
    hackernews_username: str | None

    skills: list[str]
    summary: str | None