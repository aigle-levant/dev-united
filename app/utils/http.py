"""
what does this do: helper to avoid writing
    response.raise_for_status()
    return response.json()
for the 8th time
input: url, params, headers
output: response in form of JSON
"""

import requests

from utils.supabase_helper import log_api_request, update_github_rate_limit
from integration.base import SOF, HN, GH, DEVTO

def get_json(
    url: str,
    params=None,
    headers=None,
):
    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30,
    )
    # --------------------------
    # Observability
    # --------------------------

    if GH in url:
        update_github_rate_limit(
        remaining=int(response.headers["X-RateLimit-Remaining"]),
        total=int(response.headers["X-RateLimit-Limit"]),
        reset=int(response.headers["X-RateLimit-Reset"]),
    )
        log_api_request(
            source="github",
            endpoint=url,
        )

    elif SOF in url:
        log_api_request(
            source="stackoverflow",
            endpoint=url,
        )

    elif DEVTO in url:
        log_api_request(
            source="devto",
            endpoint=url,
        )

    elif HN in url:
        log_api_request(
            source="hackernews",
            endpoint=url,
        )

    response.raise_for_status()

    return response.json()