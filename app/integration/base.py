import httpx

client = httpx.Client(timeout=10.0)

# base urls
HN = "http://hn.algolia.com/api/v1"
DEVTO = "https://dev.to/api"
SOF = "https://api.stackexchange.com/2.3"