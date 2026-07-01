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

from db.supabase import supabase


def log_api_request(
    source: str,
    endpoint: str,
):
    return (
        supabase.table("api_request_logs")
        .insert(
            {
                "source": source,
                "endpoint": endpoint,
            }
        )
        .execute()
    )

def log_resolution(
    profile_id: str,
    duration_ms: float,
):
    return (
        supabase.table("resolution_logs")
        .insert(
            {
                "profile_id": profile_id,
                "duration_ms": duration_ms,
            }
        )
        .execute()
    )

def log_llm_usage(
    provider: str,
    model: str,
    prompt_tokens: int,
    completion_tokens: int,
    total_tokens: int,
    estimated_cost: float,
):
    return (
        supabase.table("llm_usage_logs")
        .insert(
            {
                "provider": provider,
                "model": model,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens,
                "estimated_cost": estimated_cost,
            }
        )
        .execute()
    )

def update_github_rate_limit(
    remaining: int,
    total: int,
    reset: int,
):
    (
        supabase.table("github_rate_limit")
        .upsert(
            {
                "id": 1,
                "remaining": remaining,
                "total": total,
                "reset_time": reset,
            }
        )
        .execute()
    )