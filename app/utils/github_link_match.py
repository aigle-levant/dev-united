from utils.normalized_text import normalize_text

def github_link_match(left, right):
    if not left.website:
        return False

    if not right.github_username:
        return False

    return (
        f"github.com/{normalize_text(right.github_username)}"
        in normalize_text(left.website)
    )

def github_link_match_reversed(left, right):
    if not left.github_username:
        return False

    if not right.website:
        return False

    return (
        f"github.com/{normalize_text(right.website)}"
        in normalize_text(left.github_username)
    )