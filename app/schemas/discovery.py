from pydantic import BaseModel

class DiscoveredAccounts(BaseModel):
    github: str | None = None
    stackoverflow: int | None = None
    devto: str | None = None
    hackernews: str | None = None