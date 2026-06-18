from pathlib import Path
import re


ROOT = Path(
    "../../"
)


def convert_file(file):

    text = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )


    if "Learning Profile" not in text:

        return



    old = text.split(
        "Learning Profile",
        1
    )[1]


    items = []



    blocks = re.split(
        r"\n(?=[^#\n].*\nCorrect)",
        old
    )


    for block in blocks:


        name = re.match(
            r"^\s*(.+)",
            block
        )


        correct = re.search(
            r"Correct\s*\+?(\d+)",
            block
        )

        wrong = re.search(
            r"Wrong\s*\+?(\d+)",
            block
        )

        date = re.search(
            r"Last\s*Seen\s*([0-9\-\/]+)",
            block
        )


        if not name or not correct:

            continue



        item = name.group(1).strip()


        if item in [
            "Learning Profile",
            "Profile"
        ]:

            continue



        items.append(
            f"""
### ITEM: {item}

Correct +{correct.group(1)}
Wrong +{wrong.group(1) if wrong else 0}
Last Seen {date.group(1) if date else ""}
Mastery: 
Priority:
"""
        )



    if not items:

        return



    new_text = text.split(
        "Learning Profile",
        1
    )[0]


    new_text += (
        "Learning Profile\n\n"
        + "\n".join(items)
    )


    file.write_text(
        new_text,
        encoding="utf-8"
    )


    print(
        "Converted:",
        file.name
    )



for md in ROOT.rglob("*.md"):

    convert_file(md)


print("Done")