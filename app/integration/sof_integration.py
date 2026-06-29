from integration.base import SOF, SOF_PARAMS
from utils.http import get_json

from schemas.profiles import (
    StackOverflowProfile,
    TopTag,
    Question,
    Answer,
    StackOverflowAccount,
)

def fetch_profile_by_id(user_id: int) -> StackOverflowProfile:
    data = get_json(
        f"{SOF}/users/{user_id}",
        params=SOF_PARAMS,
    )["items"]

    if not data:
        return None

    return fetch_profile(data[0])

def search_users(name: str) -> list[dict]:
    return get_json(
        f"{SOF}/users",
        params={
            **SOF_PARAMS,
            "inname": name,
        },
    )["items"]


def fetch_profile(user: dict) -> StackOverflowProfile:
    return StackOverflowProfile(
        user_id=user["user_id"],
        display_name=user["display_name"],
        reputation=user["reputation"],
        location=user.get("location"),
        website=user.get("website_url"),
        profile_url=user["link"],
    )


def fetch_top_tags(user_id: int) -> list[TopTag]:
    tags = get_json(
        f"{SOF}/users/{user_id}/top-tags",
        params=SOF_PARAMS,
    )["items"]

    return [
        TopTag(
            tag_name=tag["tag_name"],
            answer_score=tag["answer_score"],
            question_score=tag["question_score"],
        )
        for tag in tags
    ]

def fetch_questions(user_id: int) -> list[Question]:
    questions = get_json(
        f"{SOF}/users/{user_id}/questions",
        params={
            **SOF_PARAMS,
            "sort": "votes",
            "order": "desc",
            "pagesize": 10,
        },
    )["items"]

    return [
        Question(
            question_id=q["question_id"],
            score=q["score"],
            creation_date=q.get("creation_date"),
        )
        for q in questions
    ]

def fetch_answers(user_id: int) -> list[Answer]:
    answers = get_json(
        f"{SOF}/users/{user_id}/answers",
        params={
            **SOF_PARAMS,
            "sort": "votes",
            "order": "desc",
            "pagesize": 10,
        },
    )["items"]

    return [
        Answer(
            answer_id=answer["answer_id"],
            score=answer["score"],
            creation_date=answer.get("creation_date"),
        )
        for answer in answers
    ]


def fetch_stackoverflow(user_id: int) -> StackOverflowAccount | None:

    profile = fetch_profile_by_id(user_id)

    if not profile:
        return None

    return StackOverflowAccount(
        profile=profile,
        top_tags=fetch_top_tags(profile.user_id),
        questions=fetch_questions(profile.user_id),
        answers=fetch_answers(profile.user_id),
    )