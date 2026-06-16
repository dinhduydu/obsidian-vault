from pathlib import Path


AUTO_START = "<!-- AUTO_START -->"
AUTO_END = "<!-- AUTO_END -->"

USER_START = "<!-- USER_START -->"
USER_END = "<!-- USER_END -->"


def create_template(content):

    return f"""
{AUTO_START}

{content}

{AUTO_END}


{USER_START}


{USER_END}
""".strip()



def update_markdown(
    file_path: Path,
    new_content: str
):

    if not file_path.exists():

        file_path.write_text(
            create_template(new_content),
            encoding="utf-8"
        )

        return


    old_text = file_path.read_text(
        encoding="utf-8"
    )


    # file cũ chưa có vùng
    if AUTO_START not in old_text:

        file_path.write_text(
            create_template(old_text),
            encoding="utf-8"
        )

        return



    before = old_text.split(
        AUTO_START
    )[0]


    after = old_text.split(
        AUTO_END
    )[1]


    new_text = (
        before
        + AUTO_START
        + "\n\n"
        + new_content
        + "\n\n"
        + AUTO_END
        + after
    )


    file_path.write_text(
        new_text,
        encoding="utf-8"
    )