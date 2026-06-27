"""
what does this do: fetches data from HN API
input: username
output: fetched data in form of JSON
"""

# imports
from integration.base import HN
from utils.http import get_json
from schemas.profiles import HNProfile, HNActivity, HackerNewsAccount

def fetch_profile(username: str)->HNProfile:
    data = get_json(
        f"{HN}/users/{username}"
    )

    return HNProfile(
        username=data["username"],
        karma=data["karma"],
        bio=data.get("about"),
        created_at=data.get("created_at"),
    )

def fetch_activity(username: str)->HNActivity:
    data = get_json(
        f"{HN}/search",
        params={
            "tags": f"author_{username}"
        }
    )["hits"]

    return [
        HNActivity(
            object_id=hit["objectID"],
            created_at=hit["created_at"],
            story_title=hit.get("story_title"),
            title=hit.get("title"),
            comment_text=hit.get("comment_text"),
            url=hit.get("url"),
        )
        for hit in data
    ]

def fetch_hn(username: str)->HackerNewsAccount:
    return HackerNewsAccount(
        profile=fetch_profile(username),
        activity=fetch_activity(username),
    )