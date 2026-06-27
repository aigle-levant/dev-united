from pydantic import BaseModel, HttpUrl

class HNProfile(BaseModel):
    username: str
    karma: int
    about: str | None
    created_at: str | None

class HNActivity(BaseModel):
    object_id: str
    created_at: str
    story_title: str | None
    title: str | None
    comment_text: str | None
    url: str | None

class GitHubProfile(BaseModel):
    id: int
    username: str
    name: str | None = None

    bio: str | None = None
    location: str | None = None

    company: str | None = None
    blog: HttpUrl | str | None = None

    email: str | None = None
    twitter_username: str | None = None

    public_repos: int

    followers: int
    following: int

    profile_url: HttpUrl

    avatar_url: HttpUrl

    created_at: str
    updated_at: str

class Repository(BaseModel):
    id: int

    name: str

    full_name: str

    description: str | None = None

    language: str | None = None

    stargazers_count: int

    forks_count: int

    html_url: HttpUrl

class GitHubEvent(BaseModel):
    type: str

    repo: str

    created_at: str

class StackOverflowProfile(BaseModel):
    user_id: int
    display_name: str
    reputation: int
    location: str | None
    website: str | None

class TopTag(BaseModel):
    tag_name: str
    answer_score: int
    question_score: int

class Answer(BaseModel):
    answer_id: int
    score: int
    creation_date: str

class DevToProfile(BaseModel):
    username: str
    name: str
    bio: str | None
    location: str | None
    github_username: str | None
    twitter_username: str | None
    website: str | None

class Article(BaseModel):
    title: str
    published_at: str
    tags: list[str]
    url: str
