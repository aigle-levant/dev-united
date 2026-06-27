
import httpx
from config import GITHUB_TOKEN, STACKEXCHANGE_KEY

client = httpx.Client(timeout=10)

# base urls
HN = "https://hn.algolia.com/api/v1"
DEVTO = "https://dev.to/api"
SOF = "https://api.stackexchange.com/2.3"
GH = "https://api.github.com"

# GH auth

GH_HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}

SOF_PARAMS = {
    "site": "stackoverflow",
    "key": STACKEXCHANGE_KEY,
}