# Dev United

A FastAPI-based service that unifies developer profiles across multiple public platforms into a single canonical profile.

The system discovers developer accounts, ingests public profile data, resolves identities across platforms using deterministic confidence scoring, stores both raw and canonical representations in Supabase, enriches the unified profile using Gemini 2.5 Flash, and exposes everything through a REST API.

 

# Features

- GitHub integration
- Stack Overflow integration
- dev.to integration
- Hacker News integration
- Deterministic entity resolution
- Canonical profile generation
- Gemini-powered profile summaries
- Supabase persistence
- Health & observability endpoint
- Render deployment

 

# Architecture

```
POST /profiles/resolve
        │
        ▼
Account Discovery
        │
        ▼
Fetch External APIs
        │
        ▼
Store Raw Profiles
        │
        ▼
Normalize Profiles
        │
        ▼
Entity Resolution
        │
        ▼
Create Canonical Profile
        │
        ▼
Gemini Summary
        │
        ▼
Update Canonical Profile
        │
        ▼
Return profile_id
```

The API intentionally separates ingestion from canonical data. Raw API responses are preserved so the canonical profile can always be regenerated without re-fetching external services.

 

# Data Sources

| Platform | Information Retrieved |
|   --|       --|
| GitHub | Profile, repositories, languages, recent activity |
| Stack Overflow | Profile, reputation |
| dev.to | Profile, articles |
| Hacker News | Profile, comments & submissions |

 

# Project Structure

```
app/
│
├── integration/
│     GitHub
│     Stack Overflow
│     Dev.to
│     HackerNews
│
├── routes/
│
├── services/
│     Discovery
│     Entity Resolution
│     AI Layer
│
├── utils/
│
├── schemas/
│
└── db/
```

Each integration is isolated from the others, making it easy to introduce new developer platforms without affecting the resolution pipeline.

 

# Avoiding Repetition

A common helper (`get_json`) handles all outbound HTTP requests.

Instead of repeating

```python
response = httpx.get(...)
response.raise_for_status()
return response.json()
```

every integration simply calls

```python
get_json(
    url,
    headers=headers,
    params=params,
)
```

This keeps the integrations small while centralizing request handling and health logging.

 

# Normalization

Each external API exposes completely different schemas.

For example:

GitHub

- login
- followers
- company
- blog

Stack Overflow

- display_name
- reputation
- website_url

dev.to

- username
- summary
- github_username

Hacker News

- username
- karma

These are transformed into one common internal model:

```python
NormalizedAccount
```

which contains

- source
- username
- name
- bio
- location
- website
- github_username
- twitter_username
- email
- reputation

This allows downstream services to perform matching without depending on provider-specific fields.

 

# Entity Resolution

Entity resolution is deterministic.

Every normalized account is compared against the chosen canonical account.

Signals currently include:

| Signal | Weight |
|   |  -:|
| GitHub username | 60 |
| Email | 50 |
| GitHub backlink | 40 |
| Twitter username | 30 |
| Website | 20 |
| Name similarity | 20 |
| Location similarity | 10 |

Profiles with confidence scores above the configured threshold are linked to the canonical profile.

Ambiguous matches are intentionally rejected instead of forcing incorrect merges.

 

# Database Design

The schema separates ingestion from canonical entities.

## raw_profiles

Stores complete API responses from every provider.

Purpose:

- preserve source data
- avoid repeated API calls
- allow rebuilding canonical profiles

 

## canonical_profiles

Stores the unified developer profile.

Fields include

- name
- bio
- website
- location
- llm_summary

 

## profile_links

Maps raw profiles to canonical profiles.

Stores

- confidence score
- matching signals
- match status

 

## api_request_logs

Tracks every external API request.

Used by the health endpoint.

 

## resolution_logs

Tracks profile resolution latency.

Used to compute average processing time.


## llm_usage_logs

Stores

- provider
- model
- token usage
- estimated cost


## github_rate_limit

Stores the latest GitHub rate limit information for observability.

# AI Layer

Gemini 2.5 Flash is used to generate a concise summary of the unified developer profile.

The prompt includes information aggregated across multiple platforms.

The generated summary is stored inside the canonical profile instead of being regenerated on every request.


# API

## POST /profiles/resolve

Input

```json
{
    "name": "Ben Halpern"
}
```

Response

```json
{
    "profile_id": "..."
}
```


## GET /profiles/{id}

Returns

- canonical profile
- Gemini summary
- contributing source profiles
- confidence scores


## GET /health

Provides production-style observability including

- GitHub rate limits
- external API requests
- LLM usage
- average resolution time
- number of profiles resolved


# Running Locally

```
pip install -r requirements.txt
```

Create

```
.env
```

```
SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=

GITHUB_TOKEN=
SOF_API_KEY=

GEMINI_API_KEY=
```

Run

```
uvicorn app.main:app --reload
```


# Deployment

The application is deployed on Render.


# Trade-offs

To keep the project focused, I chose deterministic weighted matching instead of an embedding-based or fully LLM-assisted identity resolution system.

This approach is:

- explainable
- fast
- inexpensive
- easy to tune

One limitation is that very ambiguous profiles may not be merged automatically.

# AI Usage

AI tools (primarily ChatGPT) were used for:

- debugging FastAPI stack traces
- discussing architecture trade-offs
- generating boilerplate
- reviewing code structure

Final implementation, integration decisions, schema design, entity resolution strategy, testing, and debugging were completed manually.
