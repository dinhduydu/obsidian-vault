from pathlib import Path
import re


VAULT = Path("path/to/your/vault")


CATEGORIES = [
    "Vocabulary",
    "Kanji",
    "Grammar",
    "Particle",
    "Reading",
    "CompoundVerb",
    "Adverb",
    "Conjunction",
    "FixedExpression",
    "Collocation",
    "Keigo",
    "Kenjougo"
]


def upgrade_line(line):

    stripped = line.strip()


    for cat in CATEGORIES:

        prefix = cat + " |"

        if stripped.startswith(prefix):

            indent = line[:len(line)-len(line.lstrip())]

            return (
                indent
                + "### "
                + stripped
                + "\n"
            )


    return line





def process_file(path):

    text = path.read_text(
        encoding="utf-8"
    )


    new_lines = []


    changed = False


    for line in text.splitlines(
        keepends=True
    ):


        new_line = upgrade_line(
            line
        )


        if new_line != line:

            changed = True


        new_lines.append(
            new_line
        )



    if changed:

        path.write_text(
            "".join(new_lines),
            encoding="utf-8"
        )

        print(
            "Updated:",
            path.name
        )





def main():

    for md in VAULT.rglob(
        "*.md"
    ):

        process_file(md)


    print(
        "Migration done"
    )



if __name__ == "__main__":
    main()