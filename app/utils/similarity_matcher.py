"""
what does this do: compares 2 strings and returns a val b/w 0.0 and 1.0, depending on how similar they both are
input: 2 strings
output: ratio of similarity
"""

# imports
from difflib import SequenceMatcher
from utils.normalized_text import normalize_text

def similarity(a: str | None, b: str | None) -> float:
    if not a or not b:
        return 0.0
    return SequenceMatcher(
        None,
        normalize_text(a),
        normalize_text(b),
    ).ratio()