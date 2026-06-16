import re


GRAMMAR_HINTS = [
    "〜",
    "こと",
    "もの",
    "わけ",
    "はず",
    "よう",
    "のが",
    "という",
    "に対して",
    "に関して"
]


def classify(name):

    for hint in GRAMMAR_HINTS:

        if hint in name:
            return "Grammar"

    if re.fullmatch(
        r"[一-龯々]+",
        name
    ):
        if len(name) <= 2:
            return "Kanji"

    return "Vocabulary"