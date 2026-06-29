from integration.devto_integration import fetch_devto
from integration.github_integration import fetch_github
from integration.hn_integration import fetch_hn
from integration.sof_integration import fetch_stackoverflow

from services.normalize_integrations import (
    normalize_gh,
    normalize_devto,
    normalize_stackoverflow,
    normalize_hn,
)

from services.entity_resolution import resolve_entities


async def resolve_profile_service(req):
    github = fetch_github(req.github) if req.github else None

    stackoverflow = (
        fetch_stackoverflow(req.stackoverflow)
        if req.stackoverflow
        else fetch_stackoverflow(req.name)
    )

    devto = fetch_devto(req.devto) if req.devto else None

    hackernews = (
        fetch_hn(req.hackernews)
        if req.hackernews
        else None
    )

    normalized_accounts = []

    if github:
        normalized_accounts.append(normalize_gh(github))

    if stackoverflow:
        normalized_accounts.append(normalize_stackoverflow(stackoverflow))

    if devto:
        normalized_accounts.append(normalize_devto(devto))

    if hackernews:
        normalized_accounts.append(normalize_hn(hackernews))

    resolved = resolve_entities(normalized_accounts)

    return resolved