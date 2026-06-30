from db.supabase import supabase


def get_profile(profile_id: str):

    canonical = (
        supabase.table("canonical_profiles")
        .select("*")
        .eq("id", profile_id)
        .single()
        .execute()
    )

    if not canonical.data:
        return None

    links = (
        supabase.table("profile_links")
        .select("*")
        .eq("canonical_profile_id", profile_id)
        .execute()
    )

    sources = []

    for link in links.data:

        raw = (
            supabase.table("raw_profiles")
            .select("*")
            .eq("id", link["raw_profile_id"])
            .single()
            .execute()
        )

        sources.append(
            {
                "source": raw.data["source"],
                "confidence": link["confidence"],
                "matched": link["matched"],
                "signals": link["signals"],
                "raw": raw.data["raw_payload"],
            }
        )

    return {
        "profile_id": profile_id,
        "canonical": canonical.data,
        "sources": sources,
    }