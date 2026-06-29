"""
what does this do: schema for normalization of the 4 different sources of info
"""
# imports
from pydantic import BaseModel

class NormalizedAccount(BaseModel):
    source: str

    external_id: str | None = None

    username: str | None = None
    name: str | None = None

    bio: str | None = None
    location: str | None = None

    website: str | None = None

    github_username: str | None = None
    twitter_username: str | None = None

    email: str | None = None

    reputation: int | None = None