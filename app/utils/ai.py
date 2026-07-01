from db.supabase import supabase


def save_llm_usage(
    provider: str,
    model: str,
    tokens: int,
):
    (
        supabase.table("llm_usage_logs")
        .insert(
            {
                "provider": provider,
                "model": model,
                "total_tokens": tokens,
                "estimated_cost": 0,
            }
        )
        .execute()
    )

def save_llm_summary(
    profile_id: str,
    summary: str,
):
    (
        supabase.table("canonical_profiles")
        .update(
            {
                "llm_summary": summary,
            }
        )
        .eq("id", profile_id)
        .execute()
    )