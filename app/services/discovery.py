from urllib.parse import urlparse

from integration.github_integration import (
    search_users as github_search,
    fetch_profile as fetch_github_profile,
)

from integration.sof_integration import (
    search_users as stackoverflow_search,
)

from utils.similarity_matcher import similarity


GITHUB_THRESHOLD = 0.90
STACKOVERFLOW_THRESHOLD = 0.90
MAX_CANDIDATES = 5


def discover_github(
    name: str,
    github_hint: str | None = None,
) -> str | None:
    """
    Discover GitHub username.
    """

    if github_hint:
        return github_hint

    users = github_search(name)

    if not users:
        return None

    best_username = None
    best_score = 0.0

    for user in users[:MAX_CANDIDATES]:

        try:
            profile = fetch_github_profile(user["login"])
        except Exception:
            continue

        score = similarity(profile.name, name)

        if score > best_score:
            best_score = score
            best_username = profile.username

    if best_score >= GITHUB_THRESHOLD:
        return best_username

    return None


def discover_stackoverflow(
    name: str,
    stackoverflow_hint: str | None = None,
) -> int | None:
    """
    Discover StackOverflow user id.
    """

    if stackoverflow_hint:
        try:
            return int(stackoverflow_hint)
        except ValueError:
            pass

    users = stackoverflow_search(name)

    if not users:
        return None

    best_id = None
    best_score = 0.0

    for user in users[:MAX_CANDIDATES]:

        score = similarity(
            user.get("display_name"),
            name,
        )

        if score > best_score:
            best_score = score
            best_id = user["user_id"]

    if best_score >= STACKOVERFLOW_THRESHOLD:
        return best_id

    return None


def discover_devto(
    github_blog: str | None,
    devto_hint: str | None = None,
) -> str | None:
    """
    Discover Dev.to username.

    Strategy:
    1. User supplied username.
    2. Extract from GitHub blog URL if it points to dev.to.
    """

    if devto_hint:
        return devto_hint

    if not github_blog:
        return None

    try:
        parsed = urlparse(github_blog)
    except Exception:
        return None

    if "dev.to" not in parsed.netloc.lower():
        return None

    path = parsed.path.strip("/")

    if not path:
        return None

    return path.split("/")[0]


def discover_hackernews(
    name: str,
    hackernews_hint: str | None = None,
) -> str | None:
    """
    Hacker News does not provide an official API to
    search users by real name.

    Therefore we only use a supplied username.
    """

    if hackernews_hint:
        return hackernews_hint

    return None