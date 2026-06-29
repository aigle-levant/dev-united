from schemas.normalize import NormalizedAccount
from utils.normalized_text import normalize_text


def github_link_match(
    left: NormalizedAccount,
    right: NormalizedAccount,
) -> bool:

    if left.website and right.github_username:
        if (
            f"github.com/{normalize_text(right.github_username)}"
            in normalize_text(left.website)
        ):
            return True

    if right.website and left.github_username:
        if (
            f"github.com/{normalize_text(left.github_username)}"
            in normalize_text(right.website)
        ):
            return True

    return False