from pathlib import Path

from config import SCAN_FOLDERS
from utils import get_category


def scan_folders():
    scanned_files = []

    for folder in SCAN_FOLDERS:

        if not folder.exists():
            continue

        for file in folder.rglob("*"):

            if file.is_file():

                scanned_files.append(
                    {
                        "name": file.name,
                        "path": str(file),
                        "category": get_category(file),
                        "size": round(file.stat().st_size / 1024, 2),
                    }
                )

    return scanned_files