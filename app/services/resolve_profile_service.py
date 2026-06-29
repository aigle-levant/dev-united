from services.discovery import (
    discover_github,
    discover_stackoverflow,
    discover_devto,
    discover_hackernews,
)

from integration.github_integration import fetch_github
from integration.sof_integration import fetch_stackoverflow
from integration.devto_integration import fetch_devto
from integration.hn_integration import fetch_hn

from services.normalize_integrations import (
    normalize_gh,
    normalize_stackoverflow,
    normalize_devto,
    normalize_hn,
)



async def resolve_profile_service(req):
    github_username = discover_github(
        req.name,
        req.github,
    )

    github = (
        fetch_github(github_username)
        if github_username
        else None
    )

    stackoverflow_id = discover_stackoverflow(
        req.name,
        req.stackoverflow,
    )

    stackoverflow = (
        fetch_stackoverflow(stackoverflow_id)
        if stackoverflow_id
        else None
    )

    devto_username = discover_devto(
        str(github.profile.blog) if github and github.profile.blog else None,
        req.devto,
    )

    devto = (
        fetch_devto(devto_username)
        if devto_username
        else None
    )

    hackernews_username = discover_hackernews(
        req.name,
        req.hackernews,
    )

    hackernews = (
        fetch_hn(hackernews_username)
        if hackernews_username
        else None
    )

    # --------------------------
    # NORMALIZATION
    # --------------------------

    accounts = []

    if github:
        accounts.append(normalize_gh(github))

    if stackoverflow:
        accounts.append(normalize_stackoverflow(stackoverflow))

    if devto:
        accounts.append(normalize_devto(devto))

    if hackernews:
        accounts.append(normalize_hn(hackernews))

    # --------------------------
    # ENTITY RESOLUTION
    # --------------------------

    return accounts