import re

from models import KnowledgeItem



def normalize_text(text):

    return (
        text
        .replace("🔴", "")
        .replace("🟠", "")
        .replace("🟢", "")
        .replace("**", "")
        .replace("`", "")
        .strip()
    )



def clean_name(name):

    name = normalize_text(name)


    prefixes = [
        "NAME:",
        "ITEM:",
        "Item:",
        "Vocabulary:",
        "Grammar:",
        "Katakana:",
        "Kanji:",
        "Particle:",
        "Reading:",
        "Compound Verb:",
        "CompoundVerb:",
        "Fixed Expression:",
        "FixedExpression:",
        "Collocation:",
        "Adverb:",
        "Conjunction:",
        "Keigo:",
        "Kenjougo:"
    ]


    for p in prefixes:

        if name.startswith(p):

            name = name[len(p):].strip()



    name = re.sub(
        r"^\d+[\.\)]\s*",
        "",
        name
    )


    return name.strip()





def normalize_category(category):

    if not category:
        return None


    key = (
        category
        .replace(" ", "")
        .lower()
    )


    mapping = {

        "vocabulary":
            "Vocabulary",

        "grammar":
            "Grammar",

        "kanji":
            "Kanji",

        "katakana":
            "Katakana",

        "particle":
            "Particle",

        "reading":
            "Reading",

        "compoundverb":
            "CompoundVerb",

        "adverb":
            "Adverb",

        "conjunction":
            "Conjunction",

        "fixedexpression":
            "FixedExpression",

        "collocation":
            "Collocation",

        "keigo":
            "Keigo",

        "kenjougo":
            "Kenjougo"
    }


    return mapping.get(
        key
    )





def split_heading_category(title):


    title = (
        title
        .replace("#","")
        .strip()
    )


    if "|" not in title:

        return (
            clean_name(title),
            None
        )


    left, right = title.split(
        "|",
        1
    )


    category = normalize_category(
        left.strip()
    )


    name = clean_name(
        right.strip()
    )


    return (
        name,
        category
    )







def extract_category_map(text):

    result = {}


    for line in text.splitlines():

        line = line.strip()


        if not line:
            continue



        # nhận:
        # Vocabulary | 同格
        # ### Vocabulary | 同格

        if "|" in line:


            name, category = split_heading_category(
                line
            )


            if (
                name
                and category
            ):

                result[name] = category



    return result







def parse_profiles(text):

    result = []


    blocks = re.split(
        r"\n(?=(?:###|Vocabulary \||Grammar \||Adverb \||Katakana \||Kanji \||Reading \||Collocation \||FixedExpression \||CompoundVerb \||Keigo \||Kenjougo \|))",
        text
    )



    for block in blocks:


        if "Correct:" not in block:

            continue



        first_line = (
            block
            .splitlines()[0]
            .strip()
        )


        name, heading_category = split_heading_category(
            first_line
        )



        correct = re.search(
            r"Correct:\s*\+?(\d+)",
            block
        )


        wrong = re.search(
            r"Wrong:\s*\+?(\d+)",
            block
        )


        mastery = re.search(
            r"Mastery:\s*(.+)",
            block
        )


        priority = re.search(
            r"Priority:\s*(.+)",
            block
        )


        if not correct:

            continue



        result.append({

            "name":
                name,

            "heading_category":
                heading_category,

            "correct":
                int(correct.group(1)),

            "wrong":
                int(wrong.group(1))
                if wrong else 0,

            "mastery":
                mastery.group(1).strip()
                if mastery else "",

            "priority":
                priority.group(1).strip()
                if priority else ""

        })


    return result







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



    category_map = extract_category_map(
        text
    )


    print(
        "CATEGORY MAP:",
        len(category_map)
    )



    profile_text = text.split(
        "Learning Profile",
        1
    )[1]



    items = []



    for data in parse_profiles(
        profile_text
    ):


        name = data["name"]



        category = (
            data["heading_category"]
            or category_map.get(name)
        )



        if category is None:

            category = "Vocabulary"



        item = KnowledgeItem(

            name=name,

            category=category,

            correct=data["correct"],

            wrong=data["wrong"],

            mastery=data["mastery"],

            priority=data["priority"]
        )


        item.last_seen = review_date


        item.reviews.add(
            file_path.stem
        )


        items.append(item)


        print(
            "NAME:",
            item.name,
            "CATEGORY:",
            item.category
        )


    return items