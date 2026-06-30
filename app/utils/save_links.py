from db.supabase import supabase


def save_profile_link(
    canonical_profile_id: str,
    raw_profile_id: str,
    confidence: int,
    matched: bool,
    signals: dict,
):
    result = (
        supabase.table("profile_links")
        .insert(
            {
                "canonical_profile_id": canonical_profile_id,
                "raw_profile_id": raw_profile_id,
                "confidence": confidence,
                "matched": matched,
                "signals": signals,
            }
        )
        .execute()
    )

    return result.data[0]