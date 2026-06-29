"""
what does this do: 
input: 2 NormalizedAccount
output: confidence ratio
"""

from config import MATCH_THRESHOLD, WEIGHTS
from schemas.normalize import NormalizedAccount
from utils.github_link_match import github_link_match
from utils.normalized_text import normalize_text
from utils.similarity_matcher import similarity


def calculate_confidence(
    left: NormalizedAccount,
    right: NormalizedAccount,
) -> tuple[int, list[str]]:

    score = 0
    signals: list[str] = []

    # GitHub username
    if (
        left.github_username
        and right.github_username
        and normalize_text(left.github_username)
        == normalize_text(right.github_username)
    ):
        score += WEIGHTS["github"]
        signals.append("github_username_match")

    # Twitter
    if (
        left.twitter_username
        and right.twitter_username
        and normalize_text(left.twitter_username)
        == normalize_text(right.twitter_username)
    ):
        score += WEIGHTS["twitter"]
        signals.append("twitter_username_match")

    # Email
    if (
        getattr(left, "email", None)
        and getattr(right, "email", None)
        and normalize_text(left.email)
        == normalize_text(right.email)
    ):
        score += WEIGHTS["email"]
        signals.append("email_match")

    # Website
    if (
        left.website
        and right.website
        and normalize_text(left.website)
        == normalize_text(right.website)
    ):
        score += WEIGHTS["website"]
        signals.append("website_match")

    # GitHub link-back
    if github_link_match(left, right):
        score += WEIGHTS["github_link"]
        signals.append("github_link")

    # Name
    if similarity(left.name, right.name) >= 0.9:
        score += WEIGHTS["name"]
        signals.append("name_match")

    # Location
    if similarity(left.location, right.location) >= 0.8:
        score += WEIGHTS["location"]
        signals.append("location_match")

    return min(score, 100), signals


def is_match(score: int) -> bool:
    return score >= MATCH_THRESHOLD