from db.supabase import supabase


def save_canonical_profile(
    name: str | None,
    bio: str | None,
    location: str | None,
    website: str | None,
):
    result = (
        supabase.table("canonical_profiles")
        .insert(
            {
                "name": name,
                "bio": bio,
                "location": location,
                "website": website,
            }
        )
        .execute()
    )

    return result.data[0]