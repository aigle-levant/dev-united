"""
what does this do: 
input: 2 NormalizedAccount
output: confidence ratio
"""

from config import WEIGHTS
from schemas.normalize import NormalizedAccount
from utils.normalized_text import normalize_text
from utils.similarity_matcher import similarity


def calculate_confidence(
    left: NormalizedAccount,
    right: NormalizedAccount,
) -> int:
    score = 0

    if (
        left.github_username
        and right.github_username
        and normalize_text(left.github_username)
        == normalize_text(right.github_username)
    ):
        score += WEIGHTS["github"]

    if (
        left.twitter_username
        and right.twitter_username
        and normalize_text(left.twitter_username)
        == normalize_text(right.twitter_username)
    ):
        score += WEIGHTS["twitter"]

    if (
        left.website
        and right.website
        and normalize_text(left.website)
        == normalize_text(right.website)
    ):
        score += WEIGHTS["website"]

    if similarity(left.name, right.name) >= 0.9:
        score += WEIGHTS["name"]

    if similarity(left.location, right.location) >= 0.8:
        score += WEIGHTS["location"]

    return min(score, 100)