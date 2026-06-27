from integration.base import DEVTO
from utils.http import get_json
from schemas.profiles import (
    DevToProfile,
    Article,
    DevToAccount,
)


def fetch_profile(username: str) -> DevToProfile:
    data = get_json(
        f"{DEVTO}/users/by_username",
        params={
            "url": username,
        },
    )

    return DevToProfile(
        username=data["username"],
        name=data["name"],
        summary=data.get("summary"),
        location=data.get("location"),
        github_username=data.get("github_username"),
        twitter_username=data.get("twitter_username"),
        website=data.get("website_url"),
    )


def fetch_articles(username: str) -> list[Article]:
    articles = get_json(
        f"{DEVTO}/articles",
        params={
            "username": username,
        },
    )

    return [
        Article(
            title=article["title"],
            published_at=article.get("published_at"),
            tags=article.get("tag_list", []),
            url=article["url"],
        )
        for article in articles
    ]

def extract_tags(articles: list[Article]) -> list[str]:
    return sorted({
        tag
        for article in articles
        for tag in article.tags
    })

def fetch_devto(username: str) -> DevToAccount:
    profile = fetch_profile(username)
    articles = fetch_articles(username)

    return DevToAccount(
        profile=profile,
        articles=articles,
        tags=extract_tags(articles),
    )