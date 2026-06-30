from urllib.parse import urlparse

from integration.github_integration import (
    search_users as github_search,
    fetch_profile as fetch_github_profile,
)

from integration.sof_integration import (
    search_users as stackoverflow_search,
)

from utils.similarity_matcher import similarity


MAX_CANDIDATES = 5

GITHUB_THRESHOLD = 0.90
STACKOVERFLOW_THRESHOLD = 0.90

AMBIGUITY_MARGIN = 0.05


def discover_github(
    name: str,
    github_hint: str | None = None,
) -> str | None:
    """
    Returns the most likely GitHub username.

    Discovery only.
    Identity resolution happens later.
    """

    if github_hint:
        return github_hint

    users = github_search(name)
    print(users)
    if not users:
        return None

    candidates = []

    for user in users[:MAX_CANDIDATES]:

        try:
            profile = fetch_github_profile(user["login"])
        except Exception:
            continue

        sim = similarity(profile.name, name)
        print(
    profile.username,
    profile.name,
    sim,
)

        candidates.append(
            (
                sim,
                profile,
            )
        )

    if not candidates:
        return None

    candidates.sort(
        key=lambda x: x[0],
        reverse=True,
    )

    best_similarity, best_profile = candidates[0]

    if best_similarity < GITHUB_THRESHOLD:
        return None

    if len(candidates) > 1:

        second_similarity = candidates[1][0]

        if (
            abs(
                best_similarity
                - second_similarity
            )
            < AMBIGUITY_MARGIN
        ):
            return None

    return best_profile.username


def discover_stackoverflow(
    name: str,
    stackoverflow_hint: str | None = None,
) -> int | None:
    """
    Returns the most likely StackOverflow user id.
    """

    if stackoverflow_hint:

        try:
            return int(stackoverflow_hint)
        except ValueError:
            return None

    users = stackoverflow_search(name)

    if not users:
        return None

    candidates = []

    for user in users[:MAX_CANDIDATES]:

        sim = similarity(
            user.get("display_name"),
            name,
        )

        candidates.append(
            (
                sim,
                user,
            )
        )

    candidates.sort(
        key=lambda x: x[0],
        reverse=True,
    )

    best_similarity, best_user = candidates[0]

    if best_similarity < STACKOVERFLOW_THRESHOLD:
        return None

    if len(candidates) > 1:

        second_similarity = candidates[1][0]

        if (
            abs(
                best_similarity
                - second_similarity
            )
            < AMBIGUITY_MARGIN
        ):
            return None

    return best_user["user_id"]


def discover_devto(
    github_blog: str | None,
    devto_hint: str | None = None,
) -> str | None:
    """
    Strategy

    1. Explicit username
    2. GitHub blog links to dev.to
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
    Hacker News has no reliable user search.

    Therefore only an explicit username is accepted.
    """

    if hackernews_hint:
        return hackernews_hint

    return None