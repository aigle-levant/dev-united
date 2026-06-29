"""
what does this do:
input: Normalized profile
output: 
"""

# imports
from config import MATCH_THRESHOLD
from schemas.normalize import NormalizedAccount
from utils.confidence_match import calculate_confidence


def resolve_entities(
    accounts: list[NormalizedAccount],
):
    if not accounts:
        return None

    canonical = accounts[0]
    matches = []

    for account in accounts:
        score, signals = calculate_confidence(
            canonical,
            account,
        )

        matches.append(
            {
                "source": account.source,
                "confidence": score,
                "matched": score >= MATCH_THRESHOLD,
                "signals": signals,
                "account": account,
            }
        )

    return {
        "canonical": canonical,
        "matches": matches,
    }