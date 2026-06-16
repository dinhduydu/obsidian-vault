from collections import defaultdict

from config import VAULT_ROOT

from scanner import (
    find_review_files,
    extract_date
)

from parser import (
    parse_review_file
)

from profile_generator import (
    generate_profiles
)

from dashboard_generator import (
    generate_dashboard
)


def main():

    review_files = (
        find_review_files(
            VAULT_ROOT
        )
    )

    knowledge = {}

    reviews = []

    for file in review_files:

        review_date = (
            extract_date(file)
        )

        reviews.append(
            file.stem
        )

        items = (
            parse_review_file(
                file,
                review_date
            )
        )

        for item in items:

            if item.name not in knowledge:

                knowledge[
                    item.name
                ] = item

            else:

                old = knowledge[
                    item.name
                ]

                old.correct += (
                    item.correct
                )

                old.wrong += (
                    item.wrong
                )

                old.reviews.update(
                    item.reviews
                )

                if (
                    item.last_seen
                    > old.last_seen
                ):
                    old.last_seen = (
                        item.last_seen
                    )

    generate_profiles(
        knowledge
    )

    generate_dashboard(
        knowledge,
        reviews
    )

    print(
        f"Reviews: {len(reviews)}"
    )

    print(
        f"Knowledge: {len(knowledge)}"
    )

    print("Done")


if __name__ == "__main__":
    main()