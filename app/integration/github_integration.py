from collections import Counter

from integration.base import GH_HEADERS, GH
from utils.http import get_json

from schemas.profiles import (
    GitHubAccount,
    GitHubProfile,
    Repository,
    GitHubEvent,
)

def github_request(endpoint: str, params=None):
    """
    Wrapper around get_json that updates health metrics.
    """


    data = get_json(
        f"{GH}{endpoint}",
        params=params,
        headers=GH_HEADERS,
    )

    return data


def search_users(name: str) -> list[dict]:
    data = github_request(
        "/search/users",
        params={
            "q": f"{name} in:fullname",
            "per_page": 5,
        },
    )

    return data["items"]


def fetch_profile(username: str) -> GitHubProfile:
    data = github_request(
        f"/users/{username}",
    )

    return GitHubProfile(
        id=data["id"],
        username=data["login"],
        name=data.get("name"),
        bio=data.get("bio"),
        location=data.get("location"),
        company=data.get("company"),
        blog=data.get("blog"),
        email=data.get("email"),
        twitter_username=data.get("twitter_username"),
        public_repos=data["public_repos"],
        followers=data["followers"],
        following=data["following"],
        profile_url=data["html_url"],
        avatar_url=data["avatar_url"],
        created_at=data.get("created_at"),
        updated_at=data.get("updated_at"),
    )


def fetch_repositories(username: str) -> list[Repository]:
    repos = github_request(
        f"/users/{username}/repos",
    )

    return [
        Repository(
            id=repo["id"],
            name=repo["name"],
            description=repo.get("description"),
            language=repo.get("language"),
            stargazers_count=repo["stargazers_count"],
            forks_count=repo["forks_count"],
            html_url=repo["html_url"],
            updated_at=repo.get("updated_at"),
        )
        for repo in repos
    ]


def fetch_events(
    username: str,
    limit: int = 10,
) -> list[GitHubEvent]:

    events = github_request(
        f"/users/{username}/events/public",
    )

    activity = []

    for event in events:
        if event["type"] not in {
            "PushEvent",
            "PullRequestEvent",
        }:
            continue

        activity.append(
            GitHubEvent(
                type=event["type"],
                repo=event["repo"]["name"],
                created_at=event["created_at"],
            )
        )

        if len(activity) >= limit:
            break

    return activity


def extract_languages(
    repositories: list[Repository],
) -> list[str]:
    return sorted(
        {
            repo.language
            for repo in repositories
            if repo.language
        }
    )


def fetch_github(username: str) -> GitHubAccount:
    profile = fetch_profile(username)
    repositories = fetch_repositories(username)
    events = fetch_events(username)

    return GitHubAccount(
        profile=profile,
        repositories=repositories,
        events=events,
        languages=extract_languages(repositories),
    )