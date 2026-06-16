from config import DASHBOARD_FILE


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

    weak_points = sorted(
        knowledge.values(),
        key=lambda x: x.wrong,
        reverse=True
    )

    lines.append(
        "## 🔥 Top Weak Points"
    )

    lines.append("")

    for item in weak_points[:20]:

        lines.append(
            f"- [[{item.name}]] "
            f"(Wrong: {item.wrong})"
        )

    lines.append("")

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