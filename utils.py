from pathlib import Path
from categories import CATEGORIES


def get_category(file_path: Path) -> str:
    """
    Returns the category of a file based on its extension.
    """

    ext = file_path.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category

    return "Others"