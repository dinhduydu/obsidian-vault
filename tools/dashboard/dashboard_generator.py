from collections import defaultdict

from config import DASHBOARD_FILE


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

    # =========================
    # OVERALL
    # =========================

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

    review_queue = sorted(
        knowledge.values(),
        key=lambda x: x.review_score,
        reverse=True
    )

    lines.append(
        "## 🚨 Review Queue"
    )

    lines.append("")

    for item in review_queue[:20]:

        lines.append(
            f"- [[{item.name}]]"
            f" | Score: {item.review_score}"
            f" | Wrong: {item.wrong}"
        )

    lines.append("")

    # =========================
    # WEAK POINTS
    # =========================

    lines.append(
        "## 🔥 Top Weak Points"
    )

    lines.append("")

    weak_points = sorted(
        knowledge.values(),
        key=lambda x: x.wrong,
        reverse=True
    )

    for item in weak_points[:20]:

        lines.append(
            f"- [[{item.name}]] "
            f"(Wrong: {item.wrong})"
        )

    lines.append("")

    # =========================
    # CATEGORY STATS
    # =========================

    category_stats = defaultdict(
        lambda: {
            "correct": 0,
            "wrong": 0
        }
    )

    for item in knowledge.values():

        category_stats[
            item.category
        ]["correct"] += item.correct

        category_stats[
            item.category
        ]["wrong"] += item.wrong

    lines.append(
        "## 📈 Category Statistics"
    )

    lines.append("")

    for category, stats in sorted(
        category_stats.items()
    ):

        total = (
            stats["correct"]
            + stats["wrong"]
        )

        acc = 0

        if total:

            acc = round(
                stats["correct"]
                / total
                * 100,
                1
            )

        lines.append(
            f"- {category}: "
            f"{acc}% "
            f"(Correct {stats['correct']} / Wrong {stats['wrong']})"
        )

    lines.append("")

    # =========================
    # GRAMMAR
    # =========================

    lines.append(
        "## 📚 Top Grammar"
    )

    lines.append("")

    for item in top_by_category(
        knowledge,
        "Grammar"
    ):

        lines.append(
            f"- [[{item.name}]] "
            f"(Score: {item.review_score})"
        )

    lines.append("")

    # =========================
    # VOCABULARY
    # =========================

    lines.append(
        "## 📚 Top Vocabulary"
    )

    lines.append("")

    for item in top_by_category(
        knowledge,
        "Vocabulary"
    ):

        lines.append(
            f"- [[{item.name}]] "
            f"(Score: {item.review_score})"
        )

    lines.append("")

    # =========================
    # KANJI
    # =========================

    lines.append(
        "## 📚 Top Kanji"
    )

    lines.append("")

    for item in top_by_category(
        knowledge,
        "Kanji"
    ):

        lines.append(
            f"- [[{item.name}]] "
            f"(Score: {item.review_score})"
        )

    lines.append("")

    # =========================
    # READING
    # =========================

    lines.append(
        "## 📚 Top Reading"
    )

    lines.append("")

    for item in top_by_category(
        knowledge,
        "Reading"
    ):

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

    for review in reviews[:20]:

        lines.append(
            f"- [[{review}]]"
        )

    DASHBOARD_FILE.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

