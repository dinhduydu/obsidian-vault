import re

from models import KnowledgeItem
from classifier import classify


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

        item = KnowledgeItem(
            name=name.strip(),
            category=classify(
                name.strip()
            ),
            correct=int(correct),
            wrong=int(wrong),
            mastery=mastery.strip(),
            priority=priority.strip()
        )

        item.reviews.add(
            file_path.stem
        )

        item.last_seen = review_date

        items.append(item)

    return items