"""
what does this do:
input: Normalized profile
output: 
"""

# imports
from schemas.normalize import NormalizedAccount
from utils.confidence_match import calculate_confidence

def resolve_entities(
    accounts: list[NormalizedAccount],
):
    if not accounts:
        return {
            "canonical": None,
            "matches": [],
        }

    canonical = accounts[0]

    matches = []

    for account in accounts:
        confidence = calculate_confidence(
            canonical,
            account,
        )

        matches.append(
            {
                "source": account.source,
                "confidence": confidence,
                "matched": confidence >= 50,
                "account": account,
            }
        )

    return {
        "canonical": canonical,
        "matches": matches,
    }