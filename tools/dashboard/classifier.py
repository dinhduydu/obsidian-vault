import re


# =========================
# Grammar
# =========================

GRAMMAR_HINTS = [
    "〜",
    "こと",
    "もの",
    "わけ",
    "はず",
    "よう",
    "のが",
    "という",
    "に対して",
    "に関して",
    "にしては",
    "にかけて",
    "しかない",
    "からして",
    "に従って",
    "向き",
]


# =========================
# Reading
# =========================

READING_HINTS = [
    "読解",
    "Đọc hiểu",
    "Nghe hiểu",
    "Nghe",
    "Reading",
    "Inference",
    "Comparison",
    "So sánh",
    "Lập trường",
    "Stance",
    "Reasoning",
    "Nguyên nhân",
    "Tóm tắt",
    "Chi tiết",
    "Ý chính",
    "Suy luận",
    "Quan điểm",
    "Phân tích",
    "Đối chiếu",
]


# =========================
# Topics
# =========================

TOPIC_HINTS = [
    "Kính ngữ",
    "Keigo",
    "Katakana",
    "Tiền tố",
    "Hậu tố",
    "Prefix",
    "Suffix",
    "Từ vựng Katakana",
    "Cụm từ cố định",
    "Fixed Expression",
]


def classify(name):

    name = name.strip()

    # =====================
    # Grammar
    # =====================

    for hint in GRAMMAR_HINTS:

        if hint in name:
            return "Grammar"

    # =====================
    # Reading
    # =====================

    for hint in READING_HINTS:

        if hint.lower() in name.lower():
            return "Reading"

    # =====================
    # Topics
    # =====================

    for hint in TOPIC_HINTS:

        if hint.lower() in name.lower():
            return "Topics"

    # =====================
    # Kanji
    # =====================

    if re.fullmatch(
        r"[一-龯々]+",
        name
    ):

        if len(name) <= 2:
            return "Kanji"

    # =====================
    # Vocabulary
    # =====================

    return "Vocabulary"
