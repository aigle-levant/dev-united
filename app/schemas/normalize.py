from pydantic import BaseModel

class NormalizedAccount(BaseModel):
    source: str
    external_id: str | None
    username: str | None
    display_name: str | None
    bio: str | None
    location: str | None
    website: str | None
    github_username: str | None
    twitter_username: str | None
    reputation: int | None