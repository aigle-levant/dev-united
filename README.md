# dev-united
An unified portfolio for developers

## Example of responses from various platforms

Given that all the 4 platforms have completely different responses, the challenge is **normalization** without losing data.

### Github

```json
{
  "login": "Swiddis",
  "id": 31739405,
  "node_id": "MDQ6VXNlcjMxNzM5NDA1",
  "avatar_url": "https://avatars.githubusercontent.com/u/31739405?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/Swiddis",
  "html_url": "https://github.com/Swiddis",
  "followers_url": "https://api.github.com/users/Swiddis/followers",
  "following_url": "https://api.github.com/users/Swiddis/following{/other_user}",
  "gists_url": "https://api.github.com/users/Swiddis/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/Swiddis/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/Swiddis/subscriptions",
  "organizations_url": "https://api.github.com/users/Swiddis/orgs",
  "repos_url": "https://api.github.com/users/Swiddis/repos",
  "events_url": "https://api.github.com/users/Swiddis/events{/privacy}",
  "received_events_url": "https://api.github.com/users/Swiddis/received_events",
  "type": "User",
  "user_view_type": "public",
  "site_admin": false,
  "name": "Simeon Widdis",
  "company": "@opensearch-project",
  "blog": "https://swiddis.net/",
  "location": null,
  "email": null,
  "hireable": null,
  "bio": "Software engineer writing database frontends with @opensearch-project, @aws. Likes: shells, optimization, dev experience, and watching code compile.",
  "twitter_username": null,
  "public_repos": 90,
  "public_gists": 19,
  "followers": 23,
  "following": 24,
  "created_at": "2017-09-07T16:08:27Z",
  "updated_at": "2026-05-25T23:08:52Z"
}
```

### stackOverFlow

```json
{
  "items": [
    {
      "badge_counts": {
        "bronze": 153,
        "silver": 153,
        "gold": 48
      },
      "account_id": 1,
      "is_employee": false,
      "last_modified_date": 1775405100,
      "last_access_date": 1781033610,
      "reputation_change_year": 40,
      "reputation_change_quarter": 10,
      "reputation_change_month": 20,
      "reputation_change_week": 20,
      "reputation_change_day": 0,
      "reputation": 64179,
      "creation_date": 1217514151,
      "user_type": "registered",
      "user_id": 1,
      "accept_rate": 100,
      "location": "Alameda, CA",
      "website_url": "https://blog.codinghorror.com/",
      "link": "https://stackoverflow.com/users/1/jeff-atwood",
      "profile_image": "https://www.gravatar.com/avatar/51d623f33f8b83095db84ff35e15dbe8?s=256&d=identicon&r=PG",
      "display_name": "Jeff Atwood"
    }
  ],
  "has_more": false,
  "quota_max": 10000,
  "quota_remaining": 9979
}
```

### HackerNews

```json
{"about":"Bug fixer.","karma":157316,"username":"pg"}
```

### Dev.to

```json
{"type_of":"user","id":1,"username":"ben","name":"Ben Halpern","twitter_username":"bendhalpern","github_username":"benhalpern","summary":"A Canadian software developer who thinks he’s funny.","location":"NY","website_url":"http://benhalpern.com","joined_at":"Dec 27, 2015","profile_image":"https://media2.dev.to/dynamic/image/width=320,height=320,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1%2Fbabb96d0-9cd2-49bc-a412-2dc4caf94c2a.png"}
```
