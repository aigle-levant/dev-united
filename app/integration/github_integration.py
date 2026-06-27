from collections import Counter
from base import GH_HEADERS, GH
from utils.http import get_json

def fetch_profile(username: str):
    return get_json(
        f"{GH}/user/{username}",
        headers=GH_HEADERS,
    )

def fetch_repositories(username: str):
    return get_json(
        f"{GH}/users/{username}/repos",
        headers=GH_HEADERS,
    )

def fetch_events(username: str):
    return get_json(
        f"{GH}/users/{username}/events/public",
        headers=GH_HEADERS,
    )

def extract_langs(repositories: list[dict]) -> list[str]:
    return sorted(
        repo["language"]
        for repo in repositories
        if repo.get("language")
    )

def recent_activity(events: list[dict], limit: int=10) -> list[dict]:
    activity = []
    
    for event in events:
        if event["type"] not in {"PushEvent",
            "PullRequestEvent",}:
            continue
        activity.append({
            "type": event["type"],
            "repo": event["repo"]["name"],
            "created_at": event["created_at"],
        })
        if len(activity)==limit:
            break
    return activity

def lang_stats(repositories: list[dict]) -> dict[str, int]:
    count = Counter()
    for repo in repositories:
        lang = repo.get("language")
        if lang:
            count[lang]+=1
    return dict(count)

def fetch_github(username: str):
    profile = fetch_profile(username)
    repo = fetch_repositories(username)
    events = fetch_events(username)

    return {
        "profile": profile,
        "repositories": repo,
        "languages": extract_langs(repo),
        "language_stats": lang_stats(repo),
        "recent_activity": recent_activity(events),
    }