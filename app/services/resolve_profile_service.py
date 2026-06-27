from integration.devto_integration import fetch_devto
from integration.github_integration import fetch_github
from integration.hn_integration import fetch_hn
from integration.sof_integration import fetch_stackoverflow

async def resolve_profile_service(req):
    github = fetch_github(req.github) if req.github else None

    stackoverflow = fetch_stackoverflow(req.name)

    devto = fetch_devto(req.devto) if req.devto else None

    hackernews = fetch_hn(req.hackernews) if req.hackernews else None

    return {
        "github": github,
        "stackoverflow": stackoverflow,
        "devto": devto,
        "hackernews": hackernews,
    }