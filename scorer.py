import re

_WORD_RE = re.compile(r"[a-z0-9]+")


def _normalize(text: str) -> str:
    return " ".join(_WORD_RE.findall(text.lower()))


def _tokenize(text: str) -> set[str]:
    return set(_WORD_RE.findall(text.lower()))


def judge(question, expects, answer, results) -> bool:
    """
    Return True when the generated answer contains the expected information.
    """

    if not expects or not answer:
        return False

    expects_norm = _normalize(expects)
    answer_norm = _normalize(answer)

    # Exact normalized phrase match.
    if expects_norm in answer_norm:
        return True

    # Allow wording differences where all expected terms are still present.
    expected_tokens = _tokenize(expects)
    answer_tokens = _tokenize(answer)

    return bool(expected_tokens) and expected_tokens.issubset(answer_tokens)