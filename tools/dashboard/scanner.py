import re
from pathlib import Path
from datetime import datetime


def extract_date(file_path):

    for parent in file_path.parents:

        if re.fullmatch(
            r"\d{8}",
            parent.name
        ):
            try:
                return datetime.strptime(
                    parent.name,
                    "%d%m%Y"
                )
            except:
                pass

    return datetime.min


def find_review_files(root):

    files = []

    for file in root.rglob("*.md"):

        if "Dashboard" in file.stem:
            continue

        if "Phân Tích" not in file.stem:
            continue

        files.append(file)

    return files
