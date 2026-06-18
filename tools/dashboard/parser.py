import re

from models import KnowledgeItem
from classifier import classify


def normalize_text(text):

    return (
        text
        .replace("🔴", "")
        .replace("🟠", "")
        .replace("🟢", "")
        .replace("**", "")
        .strip()
    )


PROFILE_PATTERN = re.compile(
    r"""
    ^([^\n]+)\n
    .*?
    Correct\s*\+?(\d+)
    ,\s*
    Wrong\s*\+?(\d+)
    ,\s*
    Last\s*Seen\s*([0-9\-]+)
    ,\s*
    Mastery\s*(.*?)
    ,\s*
    Priority\s*(.*?)
    $
    """,
    re.MULTILINE
    | re.DOTALL
    | re.VERBOSE
)

def parse_review_file(
    file_path,
    review_date
):

    text = file_path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    if "Learning Profile" not in text:
        return []

    profile_text = text.split(
        "Learning Profile",
        1
    )[1]

    items = []

    matches = PROFILE_PATTERN.findall(
        profile_text
    )

    for match in matches:

        (
            name,
            correct,
            wrong,
            _,
            mastery,
            priority
        ) = match

        name = (
            name
            .replace("**", "")
            .strip()
        )

        item = KnowledgeItem(
            name=name,
            category=classify(name),
            correct=int(correct),
            wrong=int(wrong),
            mastery=mastery.strip(),
            priority=priority.strip()
        )

        item.last_seen = review_date

        item.reviews.add(
            file_path.stem
        )

        items.append(item)

    print(
        f"{file_path.stem}: {len(items)} items"
    )

    return items