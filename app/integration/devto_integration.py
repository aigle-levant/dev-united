"""
what does this do: fetches data from HN API
input: username
output: fetched data in form of JSON
"""

# imports
from base import DEVTO
from utils.http import get_json

def fetch_profile(username: str):
    return get_json(
        f"{DEVTO}/users/by_username",
        params={
            "url": username
        }
    )


def fetch_articles(username: str):
    return get_json(
        f"{DEVTO}/articles",
        params={
            "username": username
        }
    )


def fetch_devto(username: str):
    return {
        "profile": fetch_profile(username),
        "articles": fetch_articles(username)
    }