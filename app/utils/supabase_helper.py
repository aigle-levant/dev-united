from db.supabase import supabase


def save_raw_profile(
    source: str,
    external_id: str,
    lookup_key: str | None,
    payload,
):
    if hasattr(payload, "model_dump"):
        payload = payload.model_dump(mode="json")

    result = (
        supabase.table("raw_profiles")
        .upsert(
            {
                "source": source,
                "external_id": external_id,
                "lookup_key": lookup_key,
                "raw_payload": payload,
            },
            on_conflict="source,external_id",
        )
        .execute()
    )

    return result.data[0]