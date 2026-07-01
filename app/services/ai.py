import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
)


def generate_profile_summary(
    canonical,
    accounts: list,
) -> tuple[str, int]:

    context = []

    for account in accounts:

        context.append(
            f"""
Source: {account.source}

Name: {account.name}

Username: {account.username}

Bio: {account.bio}

Location: {account.location}

Website: {account.website}

GitHub Username: {account.github_username}

Twitter Username: {account.twitter_username}

Email: {account.email}

Reputation: {account.reputation}
"""
        )

    prompt = f"""
You are helping create a unified developer profile.

Canonical Profile

Name:
{canonical.name}

Bio:
{canonical.bio}

Location:
{canonical.location}

Website:
{canonical.website}

Information collected from multiple platforms:

{"".join(context)}

Write ONE paragraph.

Summarize:

- primary technologies
- areas of expertise
- developer interests
- recent activity if available

Only use information provided.
Do not invent anything.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    tokens = (
        response.usage_metadata.total_token_count
        if response.usage_metadata
        else 0
    )

    return response.text, tokens

