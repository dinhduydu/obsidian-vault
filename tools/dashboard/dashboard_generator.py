from collections import defaultdict
from datetime import datetime
from pathlib import Path

from config import DASHBOARD_FILE


def extract_review_date(path):

    path = Path(path)

    for parent in path.parents:

        if parent.name.isdigit():

            try:
                return datetime.strptime(
                    parent.name,
                    "%d%m%Y"
                )

            except ValueError:
                pass

    return datetime.min



def top_by_category(
    knowledge,
    category,
    limit=10
):

    items = [

        x
        for x in knowledge.values()
        if x.category == category

    ]

    items.sort(
        key=lambda x: x.review_score,
        reverse=True
    )

    return items[:limit]



def generate_dashboard(
    knowledge,
    reviews
):

    lines = []


    # =========================
    # OVERALL
    # =========================

    total_correct = sum(
        x.correct
        for x in knowledge.values()
    )

    total_wrong = sum(
        x.wrong
        for x in knowledge.values()
    )

    total_answers = (
        total_correct
        + total_wrong
    )


    accuracy = 0

    if total_answers:

        accuracy = round(
            total_correct
            / total_answers
            * 100,
            1
        )


    lines.append(
        "# 📊 Japanese Learning Dashboard"
    )

    lines.append("")


    lines.append(
        "## 🎯 Overall"
    )

    lines.append("")

    lines.append(
        f"- Total Reviews: {len(reviews)}"
    )

    lines.append(
        f"- Total Knowledge Items: {len(knowledge)}"
    )

    lines.append(
        f"- Correct: {total_correct}"
    )

    lines.append(
        f"- Wrong: {total_wrong}"
    )

    lines.append(
        f"- Accuracy: {accuracy}%"
    )


    lines.append("")



    # =========================
    # REVIEW QUEUE
    # =========================

    lines.append(
        "## 🚨 Review Queue"
    )

    lines.append("")


    queue = sorted(
        knowledge.values(),
        key=lambda x: x.review_score,
        reverse=True
    )


    for item in queue[:20]:

        lines.append(
            f"- [[{item.name}]] "
            f"| {item.category}"
            f"| Score: {item.review_score}"
            f"| Wrong: {item.wrong}"
        )


    lines.append("")



    # =========================
    # WEAK POINTS
    # =========================


    lines.append(
        "## 🔥 Top Weak Points"
    )

    lines.append("")


    weak = sorted(
        knowledge.values(),
        key=lambda x: x.wrong,
        reverse=True
    )


    for item in weak[:20]:

        lines.append(
            f"- [[{item.name}]] "
            f"({item.category}) "
            f"Wrong: {item.wrong}"
        )


    lines.append("")



    # =========================
    # CATEGORY STATISTICS
    # =========================


    stats = defaultdict(
        lambda:
        {
            "correct":0,
            "wrong":0
        }
    )


    for item in knowledge.values():

        stats[item.category]["correct"] += (
            item.correct
        )

        stats[item.category]["wrong"] += (
            item.wrong
        )


    lines.append(
        "## 📈 Category Statistics"
    )

    lines.append("")


    for category, value in sorted(
        stats.items()
    ):

        total = (
            value["correct"]
            +
            value["wrong"]
        )


        acc = 0

        if total:

            acc = round(
                value["correct"]
                /
                total
                *
                100,
                1
            )


        lines.append(
            f"- {category}: "
            f"{acc}% "
            f"(Correct {value['correct']} / "
            f"Wrong {value['wrong']})"
        )


    lines.append("")



    # =========================
    # ALL CATEGORIES
    # =========================


    categories = [

        "Grammar",
        "Vocabulary",
        "Kanji",
        "Katakana",
        "Reading",
        "Particle",
        "CompoundVerb",
        "FixedExpression",
        "Collocation",
        "Adverb",
        "Conjunction",
        "Keigo",
        "Kenjougo",
        "Topics",
        "Demonstratives",
        

    ]


    for category in categories:


        items = top_by_category(
            knowledge,
            category
        )


        if not items:
            continue


        lines.append(
            f"## 📚 Top {category}"
        )

        lines.append("")


        for item in items:

            lines.append(
                f"- [[{item.name}]] "
                f"(Score: {item.review_score})"
            )


        lines.append("")



    # =========================
    # RECENT REVIEWS
    # =========================


    lines.append(
        "## 📅 Recent Reviews"
    )

    lines.append("")


    sorted_reviews = sorted(
        reviews,
        key=extract_review_date,
        reverse=True
    )


    for review in sorted_reviews[:20]:

        lines.append(
            f"- [[{review}]]"
        )


    DASHBOARD_FILE.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )