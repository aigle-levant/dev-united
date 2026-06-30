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

from services.entity_resolution import resolve_entities

from utils.supabase_helper import save_raw_profile

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

    stackoverflow_id = discover_stackoverflow(
        req.name,
        req.stackoverflow,
    )

    github = (
        fetch_github(github_username)
        if github_username
        else None
    )

    stackoverflow = (
        fetch_stackoverflow(stackoverflow_id)
        if stackoverflow_id
        else None
    )

    devto_username = discover_devto(
        github.profile.blog if github else None,
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


    github_raw = None
    stackoverflow_raw = None
    devto_raw = None
    hackernews_raw = None

    if github:
        github_raw = save_raw_profile(
            source="github",
            external_id=str(github.profile.id),
            lookup_key=github.profile.username,
            payload=github,
        )

    if stackoverflow:
        stackoverflow_raw = save_raw_profile(
            source="stackoverflow",
            external_id=str(stackoverflow.profile.user_id),
            lookup_key=str(stackoverflow.profile.user_id),
            payload=stackoverflow,
        )

    if devto:
        devto_raw = save_raw_profile(
            source="devto",
            external_id=devto.profile.username,
            lookup_key=devto.profile.username,
            payload=devto,
        )

    if hackernews:
        hackernews_raw = save_raw_profile(
            source="hackernews",
            external_id=hackernews.profile.username,
            lookup_key=hackernews.profile.username,
            payload=hackernews,
        )


    accounts = []
    raw_profiles = []

    if github:
        accounts.append(normalize_gh(github))
        raw_profiles.append(github_raw)

    if stackoverflow:
        accounts.append(normalize_stackoverflow(stackoverflow))
        raw_profiles.append(stackoverflow_raw)

    if devto:
        accounts.append(normalize_devto(devto))
        raw_profiles.append(devto_raw)

    if hackernews:
        accounts.append(normalize_hn(hackernews))
        raw_profiles.append(hackernews_raw)


    return resolve_entities(
        accounts=accounts,
        raw_profiles=raw_profiles,
    )