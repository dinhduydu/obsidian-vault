from pathlib import Path
import re


ROOT = Path(
    "E:/your_vault"
)


CATEGORY_RULES = {

    "Grammar": [
        "ngữ pháp",
        "cấu trúc",
        "grammar",
    ],


    "Reading": [
        "reading",
        "logic",
        "đoạn văn",
        "trợ từ kết nối",
    ],


    "Keigo": [
        "kính ngữ",
        "tôn kính",
        "khiêm nhường",
    ],


    "Collocation": [
        "cụm từ",
        "collocation",
        "cố định",
    ],


    "Kanji": [
        "kanji",
        "chữ hán",
        "bộ thủ",
    ],


    "Vocabulary": [
        "hậu tố",
        "từ vựng",
        "danh từ",
        "động từ",
    ]

}



def detect_category(title):

    low = title.lower()


    for category, keys in CATEGORY_RULES.items():

        for k in keys:

            if k in low:

                return category


    return "Vocabulary"





def process_file(path):

    text = path.read_text(
        encoding="utf-8",
        errors="ignore"
    )


    lines = text.splitlines()


    output = []



    for i,line in enumerate(lines):

        stripped = line.strip()


        # bắt dòng profile:
        # Hậu tố chỉ người...
        # ngay trước Correct

        if (
            stripped
            and i + 1 < len(lines)
            and "Correct:" in lines[i+1]
            and not stripped.startswith("#")
        ):

            category = detect_category(
                stripped
            )


            output.append(
                f"### {category} | {stripped}"
            )

        else:

            output.append(line)



    path.write_text(
        "\n".join(output),
        encoding="utf-8"
    )



for file in ROOT.rglob("*.md"):

    process_file(file)

    print(
        "Fixed:",
        file
    )