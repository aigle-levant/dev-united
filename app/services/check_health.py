import time
from collections import Counter
from datetime import datetime, UTC
from db.supabase import supabase


def log_resolution(
    profile_id: str,
    duration_ms: float,
):
    (
        supabase.table("resolution_logs")
        .insert(
            {
                "profile_id": profile_id,
                "duration_ms": duration_ms,
            }
        )
        .execute()
    )


def get_health_report():

    # --------------------------
    # API request logs
    # --------------------------

    api_rows = (
        supabase.table("api_request_logs")
        .select("source")
        .execute()
    )

    api_calls = Counter()

    for row in api_rows.data:
        api_calls[row["source"]] += 1

    # --------------------------
    # Resolution logs
    # --------------------------

    resolution_rows = (
        supabase.table("resolution_logs")
        .select("duration_ms")
        .execute()
    )

    total_profiles = len(resolution_rows.data)

    avg_resolution = (
        sum(row["duration_ms"] for row in resolution_rows.data)
        / total_profiles
        if total_profiles
        else 0
    )

    # --------------------------
    # LLM usage
    # --------------------------

    llm_rows = (
        supabase.table("llm_usage_logs")
        .select("total_tokens, estimated_cost")
        .execute()
    )

    total_tokens = sum(
        row["total_tokens"]
        for row in llm_rows.data
    )

    estimated_cost = sum(
        row["estimated_cost"]
        for row in llm_rows.data
    )
    rate = (
    supabase.table("github_rate_limit")
    .select("*")
    .eq("id", 1)
    .single()
    .execute()
).data

    reset = datetime.fromtimestamp(
    rate["reset_time"],
    UTC,
).isoformat()
    return {
    "status": "healthy",
    "timestamp_epoch": int(time.time()),

    "github_rate_limiting": {
        "remaining": rate["remaining"],
        "total": rate["total"],
        "reset_time": datetime.fromtimestamp(
            rate["reset_time"],
            UTC,
        ).isoformat(),
    },

    "external_api_calls_by_source": dict(api_calls),

    "llm_observability": {
        "total_tokens": total_tokens,
        "estimated_cost_usd": estimated_cost,
    },

    "resolution_performance": {
        "profiles_resolved_count": total_profiles,
        "average_resolution_time_ms": round(avg_resolution, 2),
    },
}