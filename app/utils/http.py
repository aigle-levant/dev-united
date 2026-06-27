"""
what does this do: helper to avoid writing
    response.raise_for_status()
    return response.json()
for the 8th time
input: url, params, headers
output: response in form of JSON
"""

import httpx
from integration.base import client

def get_json(
    url: str,
    *,
    params: dict | None = None,
    headers: dict | None = None
):
    response = client.get(
        url,
        params=params,
        headers=headers,
    )

    response.raise_for_status()

    return response.json()