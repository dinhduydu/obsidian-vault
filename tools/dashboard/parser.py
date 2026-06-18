import re

from models import KnowledgeItem


def normalize_text(text):

    return (
        text
        .replace("🔴", "")
        .replace("🟠", "")
        .replace("🟢", "")
        .replace("**", "")
        .strip()
    )


# =========================
# Extract Learning Profile
# =========================

PROFILE_PATTERN = re.compile(
    r"""
    ^([^\n]+)
    .*?
    Correct\s*\+?(\d+)
    .*?
    Wrong\s*\+?(\d+)
    .*?
    Last\s*Seen\s*([0-9\-]+)
    .*?
    Mastery\s*(.*?)
    .*?
    Priority\s*(.*?)
    $
    """,
    re.MULTILINE
    | re.DOTALL
    | re.VERBOSE
)


# =========================
# Extract category map
# =========================

CATEGORY_PATTERN = re.compile(
    r"""
    ^##\s*(.+?)
    \n
    (.*?)
    (?=
        ^##|
        \Z
    )
    """,
    re.MULTILINE
    | re.DOTALL
)


def extract_category_map(text):

    category_map = {}

    matches = CATEGORY_PATTERN.findall(
        text
    )

    for category, block in matches:

        category = (
            category
            .strip()
            .replace(" ", "")
        )

        for line in block.splitlines():

            line = line.strip()

            if not line.startswith("-"):
                continue

            item = (
                line[1:]
                .strip()
                .replace("**", "")
                .replace("`", "")
            )

            if item:

                category_map[item] = category


    return category_map



def normalize_category(category):

    mapping = {

        "CompoundVerb":
            "CompoundVerb",

        "Compound Verb":
            "CompoundVerb",

        "FixedExpression":
            "FixedExpression",

        "Fixed Expression":
            "FixedExpression",

        "ReadingComprehension":
            "Reading",

        "Reading Comprehension":
            "Reading",

        "Vocabulary":
            "Vocabulary",

        "Grammar":
            "Grammar",

        "Kanji":
            "Kanji",

        "Particle":
            "Particle",

        "Adverb":
            "Adverb",

        "Conjunction":
            "Conjunction",

        "Collocation":
            "Collocation",

        "Keigo":
            "Keigo",

        "Kenjougo":
            "Kenjougo",

        "Topics":
            "Topics",
    }


    return mapping.get(
        category,
        category
    )



def parse_review_file(
    file_path,
    review_date
):

    text = file_path.read_text(
        encoding="utf-8",
        errors="ignore"
    )


    if "Learning Profile" not in text:

        return []


    category_map = (
        extract_category_map(text)
    )


    profile_text = text.split(
        "Learning Profile",
        1
    )[1]


    items = []


    matches = PROFILE_PATTERN.findall(
        profile_text
    )


    for match in matches:

        (
            name,
            correct,
            wrong,
            _,
            mastery,
            priority
        ) = match


        name = (
            name
            .replace("**", "")
            .replace("`", "")
            .strip()
        )


        category = category_map.get(
            name,
            "Vocabulary"
        )


        category = normalize_category(
            category
        )


        item = KnowledgeItem(

            name=name,

            category=category,

            correct=int(correct),

            wrong=int(wrong),

            mastery=normalize_text(
                mastery
            ),

            priority=normalize_text(
                priority
            )
        )


        item.last_seen = review_date


        item.reviews.add(
            file_path.stem
        )


        items.append(item)



    print(
        f"{file_path.stem}: {len(items)} items"
    )


    return items