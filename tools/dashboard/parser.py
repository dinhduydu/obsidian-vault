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
    -\s*
    \*\*(.*?)\*\*
    \s*:\s*
    Correct\s*(\d+)
    \s*,\s*
    Wrong\s*(\d+)
    \s*,\s*
    Last\s*Seen:\s*([0-9\-]+)
    \s*,\s*
    Mastery:\s*(.*?)
    \s*,\s*
    Priority:\s*(.*?)
    $
    """,
    re.MULTILINE
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

    items = []

    matches = PROFILE_PATTERN.findall(
        text
    )

    print(
        f"{file_path.stem}: {len(matches)} items"
    )

    for match in matches:

        (
            name,
            correct,
            wrong,
            last_seen,
            mastery,
            priority
        ) = match

        clean_name = (
            name
            .replace("**", "")
            .replace("`", "")
            .strip()
        )

        item = KnowledgeItem(
            name=clean_name,
            category=classify(
                clean_name
            ),
            correct=int(correct),
            wrong=int(wrong),
            mastery=normalize_text(
                mastery
            ),
            priority=normalize_text(
                priority
            )
        )

        item.reviews.add(
            file_path.stem
        )

        item.last_seen = review_date

        items.append(item)

    return items