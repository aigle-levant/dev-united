from pydantic import BaseModel, HttpUrl
from datetime import datetime

class HNProfile(BaseModel):
    username: str
    karma: int
    bio: str | None
    created_at: datetime | None = None

class HNActivity(BaseModel):
    object_id: str
    created_at: datetime | None = None
    story_title: str | None
    title: str | None
    comment_text: str | None
    url: str | None

class HackerNewsAccount(BaseModel):
    profile: HNProfile
    activity: list[HNActivity]

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

    created_at: datetime | None = None
    updated_at: datetime | None = None

class Repository(BaseModel):
    id: int

    name: str

    description: str | None = None

    language: str | None = None

    stargazers_count: int

    forks_count: int

    html_url: HttpUrl

    updated_at: datetime | None = None

class GitHubEvent(BaseModel):
    type: str

    repo: str

    created_at: datetime | None = None

class GitHubAccount(BaseModel):
    profile: GitHubProfile
    repositories: list[Repository]
    events: list[GitHubEvent]
    languages: list[str]

class StackOverflowProfile(BaseModel):
    user_id: int
    display_name: str
    reputation: int
    location: str | None
    website: str | None
    profile_url: HttpUrl

class TopTag(BaseModel):
    tag_name: str
    answer_score: int
    question_score: int

class Question(BaseModel):
    question_id: int
    score: int
    creation_date: datetime | None = None

class Answer(BaseModel):
    answer_id: int
    score: int
    creation_date: datetime | None = None

class StackOverflowAccount(BaseModel):
    profile: StackOverflowProfile
    top_tags: list[TopTag]
    questions: list[Question]
    answers: list[Answer]

class DevToProfile(BaseModel):
    username: str
    name: str
    summary: str | None
    location: str | None
    github_username: str | None
    twitter_username: str | None
    website: str | None

class Article(BaseModel):
    title: str
    published_at: datetime | None = None
    tags: list[str]
    url: str

class DevToAccount(BaseModel):
    profile: DevToProfile
    articles: list[Article]
    tags: list[str]