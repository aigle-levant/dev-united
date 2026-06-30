
## Case 1: PG

```json
{
  "name": "Paul Graham",
  "hackernews": "pg"
}
```

- We have to pass HN id as there's no direct way to obtain profile with full name [HN API].

```json
[
  {
    "source": "github",
    "external_id": "598333",
    "username": "grazanaut",
    "name": "Paul Graham",
    "bio": null,
    "location": "Melbourne",
    "website": "http://github.com/grazanaut",
    "github_username": "grazanaut",
    "twitter_username": null,
    "email": "grazanaut@gmail.com",
    "reputation": null
  },
  {
    "source": "stackoverflow",
    "external_id": "5937775",
    "username": null,
    "name": "Paul Graham",
    "bio": null,
    "location": null,
    "website": null,
    "github_username": null,
    "twitter_username": null,
    "email": null,
    "reputation": 83
  },
  {
    "source": "hackernews",
    "external_id": "pg",
    "username": "pg",
    "name": "pg",
    "bio": "Bug fixer.",
    "location": null,
    "website": null,
    "github_username": null,
    "twitter_username": null,
    "email": null,
    "reputation": 157316
  }
]
```

- `grazanaut` is NOT Paul Graham's account as PG never maintains a GH account. Nor is the SOF account his, as he has only the HN account.
- The only solution would be to simply ask for the HN id, however, there is currently no way of avoiding the GitHub switcharoo problem as HN account of PG has barely any detail except the name.

So what I did was to simply not use name in this case:

```json
{
  "hackernews": "pg"
}
```

```json
[
  null,
  null,
  null,
  {
    "profile": {
      "username": "pg",
      "karma": 157316,
      "bio": "Bug fixer.",
      "created_at": null
    },
    "activity": [
      //...
      {
        "object_id": "21231208",
        "created_at": "2019-10-12T07:14:55Z",
        "story_title": null,
        "title": "Show HN: Bel",
        "comment_text": null,
        "url": "http://paulgraham.com/bel.html"
      },
      //...
    ]}]
```

## Case 1: `swiddis`

```json
{
  "name": "Simeon Widdis"
}
```

```json
[
  {
    "source": "github",
    "external_id": "31739405",
    "username": "Swiddis",
    "name": "Simeon Widdis",
    "bio": "Software engineer writing database frontends with @opensearch-project, @aws. Likes: shells, optimization, dev experience, and watching code compile.",
    "location": null,
    "website": "https://swiddis.net/",
    "github_username": "Swiddis",
    "twitter_username": null,
    "email": "sawiddis@gmail.com",
    "reputation": null
  }
]
```

- Seems to work fine if the dev maintains a GH account alone.

## Case 3: Ben Halpern

```json
{
  "name": "Ben Halpern",
  "github": "benhalpern"
}
```

```json
[
  {
    "source": "github",
    "external_id": "3102842",
    "username": "benhalpern",
    "name": "Ben Halpern",
    "bio": "\r\n    Founder of dev.to 👩‍💻👨‍💻-> Now open source! Come checkout our main repo at forem/forem 🌱",
    "location": "New York",
    "website": "https://dev.to/ben",
    "github_username": "benhalpern",
    "twitter_username": "bendhalpern",
    "email": "ben@dev.to",
    "reputation": null
  },
  {
    "source": "stackoverflow",
    "external_id": "4750792",
    "username": null,
    "name": "Ben Halpern",
    "bio": null,
    "location": null,
    "website": null,
    "github_username": null,
    "twitter_username": null,
    "email": null,
    "reputation": 1
  },
  {
    "source": "devto",
    "external_id": "ben",
    "username": "ben",
    "name": "Ben Halpern",
    "bio": "A Canadian software developer who thinks he’s funny.",
    "location": "NY",
    "website": "http://benhalpern.com",
    "github_username": "benhalpern",
    "twitter_username": "bendhalpern",
    "email": null,
    "reputation": null
  }
]
```

- Returns only SOF if name is passed. If GH is passed, returns SOF, GH, Devto.
