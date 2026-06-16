import re

from config import (
    PROFILE_ROOT,
    PROFILE_FOLDERS
)

def sanitize_filename(name):

    return re.sub(
        r'[\\/:*?"<>|]',
        "_",
        name
    )

def generate_profiles(
    knowledge
):

    for folder in PROFILE_FOLDERS:

        (
            PROFILE_ROOT / folder
        ).mkdir(
            parents=True,
            exist_ok=True
        )

    for item in knowledge.values():
        safe_name = sanitize_filename(
                        item.name
                    )
        path = (
            PROFILE_ROOT
            / item.category
            / f"{safe_name}.md"
        )

        total = (
            item.correct
            + item.wrong
        )

        accuracy = 0

        if total:

            accuracy = round(
                item.correct
                / total
                * 100,
                1
            )

        content = []

        content.append(
            f"# {item.name}"
        )

        content.append("")

        content.append(
            f"Category: {item.category}"
        )

        content.append(
            f"Correct: {item.correct}"
        )

        content.append(
            f"Wrong: {item.wrong}"
        )

        content.append(
            f"Accuracy: {accuracy}%"
        )

        content.append(
            f"Mastery: {item.mastery}"
        )

        content.append(
            f"Priority: {item.priority}"
        )

        content.append("")

        content.append(
            "## Related Reviews"
        )

        content.append("")

        for review in sorted(
            item.reviews
        ):
            content.append(
                f"- [[{review}]]"
            )

        path.write_text(
            "\n".join(content),
            encoding="utf-8"
        )