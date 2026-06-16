import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# ==========================
# CONFIG
# ==========================

VAULT_ROOT = Path("Chữa đề")

PROFILE_ROOT = VAULT_ROOT / "Learning_Profile"

DASHBOARD_FILE = VAULT_ROOT / "Dashboard.md"

CATEGORIES = [
    "Vocabulary",
    "Grammar",
    "Kanji",
    "Reading",
    "Topics"
]

# ==========================
# CREATE FOLDERS
# ==========================

for category in CATEGORIES:
    (PROFILE_ROOT / category).mkdir(
        parents=True,
        exist_ok=True
    )

# ==========================
# HELPERS
# ==========================

def extract_date(file_path):

    for parent in file_path.parents:

        name = parent.name

        if re.fullmatch(r"\d{8}", name):

            try:
                return datetime.strptime(
                    name,
                    "%d%m%Y"
                )
            except:
                pass

    return datetime.min


def mastery(correct, wrong):

    total = correct + wrong

    if total == 0:
        return "⚪ Unknown"

    acc = correct / total

    if acc >= 0.8:
        return "🟢 High"

    if acc >= 0.5:
        return "🟠 Medium"

    return "🔴 Low"


# ==========================
# DATABASE
# ==========================

knowledge = defaultdict(
    lambda: {
        "type": "Topics",
        "correct": 0,
        "wrong": 0,
        "last_seen": datetime.min,
        "reviews": []
    }
)

reviews = []

# ==========================
# FIND REVIEW FILES
# ==========================

review_files = []

for file in VAULT_ROOT.rglob("*.md"):

    if "Dashboard" in file.stem:
        continue

    if "Phân Tích" not in file.stem:
        continue

    review_files.append(file)

print(f"Found {len(review_files)} review files")

# ==========================
# PARSE REVIEWS
# ==========================

pattern = re.compile(
    r"###\s*(.*?)\s*[\r\n]+"
    r"Type:\s*(.*?)\s*[\r\n]+"
    r"Correct:\s*(\d+)\s*[\r\n]+"
    r"Wrong:\s*(\d+)",
    re.MULTILINE
)

for file in review_files:

    date = extract_date(file)

    reviews.append(
        {
            "name": file.stem,
            "date": date
        }
    )

    try:
        content = file.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except:
        continue

    matches = pattern.findall(content)

    for name, item_type, correct, wrong in matches:

        name = name.strip()

        correct = int(correct)

        wrong = int(wrong)

        knowledge[name]["type"] = item_type

        knowledge[name]["correct"] += correct

        knowledge[name]["wrong"] += wrong

        if date > knowledge[name]["last_seen"]:
            knowledge[name]["last_seen"] = date

        knowledge[name]["reviews"].append(
            file.stem
        )

# ==========================
# GENERATE PROFILE FILES
# ==========================

for name, data in knowledge.items():

    category = data["type"]

    if category not in CATEGORIES:
        category = "Topics"

    total = (
        data["correct"]
        + data["wrong"]
    )

    accuracy = 0

    if total:
        accuracy = round(
            data["correct"]
            / total
            * 100,
            1
        )

    profile_file = (
        PROFILE_ROOT
        / category
        / f"{name}.md"
    )

    content = []

    content.append(f"# {name}")
    content.append("")

    content.append(
        f"Type: {category}"
    )

    content.append(
        f"Correct: {data['correct']}"
    )

    content.append(
        f"Wrong: {data['wrong']}"
    )

    content.append(
        f"Accuracy: {accuracy}%"
    )

    content.append(
        f"Mastery: {mastery(data['correct'], data['wrong'])}"
    )

    if data["last_seen"] != datetime.min:

        content.append(
            f"Last Seen: {data['last_seen'].strftime('%d/%m/%Y')}"
        )

    content.append("")
    content.append("## Related Reviews")
    content.append("")

    for review in sorted(
        set(data["reviews"])
    ):
        content.append(
            f"- [[{review}]]"
        )

    profile_file.write_text(
        "\n".join(content),
        encoding="utf-8"
    )

# ==========================
# DASHBOARD
# ==========================

total_correct = sum(
    x["correct"]
    for x in knowledge.values()
)

total_wrong = sum(
    x["wrong"]
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

weak_points = sorted(
    knowledge.items(),
    key=lambda x: (
        x[1]["wrong"],
        x[1]["last_seen"]
    ),
    reverse=True
)

reviews.sort(
    key=lambda x: x["date"],
    reverse=True
)

dashboard = []

dashboard.append(
    "# 📊 Japanese Learning Dashboard\n"
)

dashboard.append(
    "## 🎯 Overall\n"
)

dashboard.append(
    f"- Total Reviews: {len(reviews)}"
)

dashboard.append(
    f"- Total Knowledge Items: {len(knowledge)}"
)

dashboard.append(
    f"- Correct: {total_correct}"
)

dashboard.append(
    f"- Wrong: {total_wrong}"
)

dashboard.append(
    f"- Accuracy: {accuracy}%\n"
)

dashboard.append(
    "## 🔥 Top 20 Weak Points\n"
)

for name, data in weak_points[:20]:

    dashboard.append(
        f"- [[{name}]] "
        f"(Wrong: {data['wrong']})"
    )

dashboard.append("")

dashboard.append(
    "## 🚨 Review Queue\n"
)

for name, data in weak_points[:20]:

    dashboard.append(
        f"- [ ] [[{name}]]"
    )

dashboard.append("")

dashboard.append(
    "## 📅 Recent Reviews\n"
)

for review in reviews[:20]:

    dashboard.append(
        f"- [[{review['name']}]] "
        f"({review['date'].strftime('%d/%m/%Y')})"
    )

dashboard.append("")

for category in CATEGORIES:

    dashboard.append(
        f"## 📚 {category}\n"
    )

    items = [
        (k, v)
        for k, v in knowledge.items()
        if v["type"] == category
    ]

    items.sort(
        key=lambda x: x[1]["wrong"],
        reverse=True
    )

    for name, data in items[:20]:

        dashboard.append(
            f"- [[{name}]] "
            f"(Wrong: {data['wrong']})"
        )

    dashboard.append("")

DASHBOARD_FILE.write_text(
    "\n".join(dashboard),
    encoding="utf-8"
)

print("Done")
print(
    f"Dashboard: {DASHBOARD_FILE}"
)
