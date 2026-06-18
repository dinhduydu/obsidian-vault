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
]


# =========================
# Adverb
# =========================

ADVERB_HINTS = [
    "きっぱり",
    "しっかり",
    "かなり",
    "ずいぶん",
    "たびたび",
    "しばしば",
    "ふと",
    "ぼんやり",
    "あっさり",
    "さっぱり",
]


# =========================
# Conjunction
# =========================

CONJUNCTION_HINTS = [
    "すると",
    "しかし",
    "ところが",
    "そのため",
    "つまり",
    "それでも",
    "したがって",
    "そこで",
]


# =========================
# Compound Verb
# =========================

COMPOUND_VERB_SUFFIXES = [
    "出す",
    "込む",
    "切る",
    "続ける",
    "返す",
    "直す",
    "始める",
    "終わる",
    "合う",
    "かける",
]


def is_compound_verb(word):

    if len(word) < 4:
        return False

    return any(
        word.endswith(suffix)
        for suffix in COMPOUND_VERB_SUFFIXES
    )


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
    # Adverb
    # =====================

    if name in ADVERB_HINTS:
        return "Adverb"

    # =====================
    # Conjunction
    # =====================

    if name in CONJUNCTION_HINTS:
        return "Conjunction"

    # =====================
    # Compound Verb
    # =====================

    if is_compound_verb(name):
        return "CompoundVerb"

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