"""
what does this do: setup normalize schemas for resolving
input: Integration schemas
output: NormalizedAccount
"""
# imports
from schemas.normalize import NormalizedAccount
from schemas.profiles import (
    GitHubAccount,
    DevToAccount,
    StackOverflowAccount,
    HackerNewsAccount,
)

def normalize_gh(acc: GitHubAccount) -> NormalizedAccount:
    profile = acc.profile
    return NormalizedAccount(
        source="github",
        external_id=str(profile.id),
        username=profile.username,
        name=profile.name,
        bio=profile.bio,
        location=profile.location,
        website=str(profile.blog) if profile.blog else None,
        github_username=profile.username,
        twitter_username=profile.twitter_username,
        reputation=None,
    )

def normalize_devto(
    account: DevToAccount,
) -> NormalizedAccount:

    profile = account.profile

    return NormalizedAccount(
        source="devto",
        external_id=profile.username,
        username=profile.username,
        name=profile.name,
        bio=profile.summary,
        location=profile.location,
        website=profile.website,
        github_username=profile.github_username,
        twitter_username=profile.twitter_username,
        reputation=None,
    )

def normalize_stackoverflow(
    account: StackOverflowAccount,
) -> NormalizedAccount:

    profile = account.profile

    return NormalizedAccount(
        source="stackoverflow",
        external_id=str(profile.user_id),
        username=None,
        name=profile.display_name,
        bio=None,
        location=profile.location,
        website=str(profile.website) if profile.website else None,
        github_username=None,
        twitter_username=None,
        reputation=profile.reputation,
    )

def normalize_hn(
    account: HackerNewsAccount,
) -> NormalizedAccount:

    profile = account.profile

    return NormalizedAccount(
        source="hackernews",
        external_id=profile.username,
        username=profile.username,
        name=profile.username,
        bio=profile.bio,
        location=None,
        website=None,
        github_username=None,
        twitter_username=None,
        reputation=profile.karma,
    )