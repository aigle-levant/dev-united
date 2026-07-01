from config import MATCH_THRESHOLD

from schemas.normalize import NormalizedAccount

from utils.confidence_match import calculate_confidence
from utils.save_canon import save_canonical_profile
from utils.save_links import save_profile_link


def choose_canonical(
    accounts: list[NormalizedAccount],
) -> NormalizedAccount:
    """
    Prefer the richest source as canonical.
    """

    priority = {
        "github": 1,
        "devto": 2,
        "stackoverflow": 3,
        "hackernews": 4,
    }

    return min(
        accounts,
        key=lambda account: priority.get(account.source, 99),
    )


def resolve_entities(
    accounts: list[NormalizedAccount],
    raw_profiles: list[dict],
):
    """
    Resolve multiple normalized accounts into one canonical entity.
    """

    if not accounts:
        return None

    # --------------------------
    # Pick canonical account
    # --------------------------

    canonical = choose_canonical(accounts)

    # --------------------------
    # Save canonical profile
    # --------------------------

    canonical_row = save_canonical_profile(
        name=canonical.name,
        bio=canonical.bio,
        location=canonical.location,
        website=canonical.website,
    )

    canonical_id = canonical_row["id"]

    matches = []

    # --------------------------
    # Compare every account
    # --------------------------

    for account, raw in zip(accounts, raw_profiles):

        if account.source == canonical.source:
            score = 100
            signals = ["canonical_source"]
        else:
            score, signals = calculate_confidence(
                canonical,
                account,
            )

        matched = score >= MATCH_THRESHOLD

        save_profile_link(
            canonical_profile_id=canonical_id,
            raw_profile_id=raw["id"],
            confidence=score,
            matched=matched,
            signals={
                "signals": signals,
            },
        )

        matches.append(
            {
                "source": account.source,
                "confidence": score,
                "matched": matched,
                "signals": signals,
            }
        )

    return {
    "profile_id": canonical_id,
    "canonical": canonical,
    "sources": matches,
}