from pathlib import Path
import re
from datetime import datetime


# =========================
# CONFIG
# =========================

ROOT = Path(
    "../../Chữa đề"
)


AUTO_MARKER = (
    "<!-- ==============================\n"
    "AUTO PARSED DATA"
)


# =========================
# UTIL
# =========================

def normalize(text):

    return (
        text
        .replace("**", "")
        .replace("🔴", "")
        .replace("🟠", "")
        .replace("🟢", "")
        .strip()
    )



def extract_date(text):

    m = re.search(
        r"(\d{2}/\d{2}/\d{4})",
        text
    )

    if m:
        return m.group(1)


    return datetime.now().strftime(
        "%d/%m/%Y"
    )



# =========================
# PARSER
# =========================

def extract_learning_profile(text):

    """
    đọc phần Learning Profile cũ
    tạo block parser-friendly
    """


    if "Learning Profile" not in text:

        return []


    section = text.split(
        "Learning Profile",
        1
    )[1]


    items = []


    blocks = re.split(
        r"\n\d+\.",
        section
    )


    for block in blocks:

        if "Learning Profile" not in block:

            continue


        name = re.search(
            r"^\s*(.+?)\n",
            block
        )


        profile = re.search(
            r"Learning Profile.*?:\s*(.*)",
            block,
            re.S
        )


        if not name or not profile:

            continue


        data = normalize(
            profile.group(1)
        )


        correct = re.search(
            r"Correct\s*\+?(\d+)",
            data
        )

        wrong = re.search(
            r"Wrong\s*\+?(\d+)",
            data
        )

        last = re.search(
            r"Last Seen[:：]?\s*([0-9/]+)",
            data
        )

        mastery = re.search(
            r"Mastery[:：]?\s*([A-Za-z]+)",
            data
        )

        priority = re.search(
            r"Priority[:：]?\s*([A-Za-z]+)",
            data
        )


        if not correct:

            continue


        items.append({

            "name":
                normalize(name.group(1)),

            "correct":
                correct.group(1),

            "wrong":
                wrong.group(1)
                if wrong else "0",

            "last":
                last.group(1)
                if last else "",

            "mastery":
                mastery.group(1)
                if mastery else "",

            "priority":
                priority.group(1)
                if priority else ""
        })


    return items




# =========================
# GENERATOR
# =========================

def generate_block(items):


    if not items:

        return ""



    lines = []


    lines.append(
        "\n\n---\n\n"
    )


    lines.append(
        "<!-- ==============================\n"
        "AUTO PARSED DATA\n\n"
        "Parser uses this section.\n"
        "User edits only this area.\n"
        "Original NotebookLM analysis above.\n"
        "Do NOT edit original analysis.\n"
        "============================== -->\n"
    )


    lines.append(
        "\n# AUTO PROFILE\n"
    )


    for item in items:


        lines.append(
            f"""
## {item['name']}

Category: Unknown

Correct: +{item['correct']}
Wrong: +{item['wrong']}
Last Seen: {item['last']}
Mastery: {item['mastery']}
Priority: {item['priority']}

"""
        )


    return "".join(lines)




# =========================
# FILE PROCESS
# =========================

def process_file(path):


    text = path.read_text(
        encoding="utf-8",
        errors="ignore"
    )


    if AUTO_MARKER in text:

        print(
            "SKIP:",
            path.name
        )

        return



    if (
        "Tóm tắt bài làm"
        not in text
        and
        "PHÂN TÍCH BÀI LÀM"
        not in text
    ):

        return



    items = extract_learning_profile(
        text
    )


    if not items:

        print(
            "NO PROFILE:",
            path.name
        )

        return



    block = generate_block(
        items
    )


    path.write_text(
        text.rstrip()
        +
        block,
        encoding="utf-8"
    )


    print(
        "UPDATED:",
        path.name,
        "|",
        len(items),
        "items"
    )





# =========================
# MAIN
# =========================

def main():


    files = list(
        ROOT.rglob(
            "*.md"
        )
    )


    print(
        "FOUND:",
        len(files),
        "markdown files"
    )


    for file in files:

        process_file(
            file
        )


    print(
        "\nDONE"
    )




if __name__ == "__main__":

    main()