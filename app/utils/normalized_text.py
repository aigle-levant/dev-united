"""
what does this do: return lowercase text without trailing whitespace
input: text
output: cleaned up text
"""

def normalize_text(text: str | None) -> str | None:
    if not text:
        return None
    return text.strip().lower()