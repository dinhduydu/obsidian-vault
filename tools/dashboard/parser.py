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

ITEM_PATTERN = re.compile(
    r"""
    ^\d+\.\s*(.*?)\n
    .*?
    Profile.*?
    Correct\s*\+?(\d+)
    .*?
    Wrong\s*\+?(\d+)
    .*?
    Last\s*Seen:\s*([0-9/]+)
    .*?
    Mastery:\s*(.*?)
    .*?
    Priority:\s*(.*?)
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

    items = []

    matches = ITEM_PATTERN.findall(text)

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

