from pathlib import Path

from config import (
    SCAN_FOLDERS,
    IGNORE_FOLDERS,
    IGNORE_FILES
)

from utils import get_category



def should_ignore(path: Path):

    # Ignore folder names
    for part in path.parts:

        if part in IGNORE_FOLDERS:
            return True


    # Ignore files
    if path.name in IGNORE_FILES:
        return True


    return False




def scan_folders():

    scanned_files = []


    for folder in SCAN_FOLDERS:


        if not folder.exists():
            continue



        for file in folder.rglob("*"):


            # Skip folders/files
            if should_ignore(file):
                continue



            if file.is_file():


                try:

                    scanned_files.append(

                        {
                            "name": file.name,

                            "path": str(file),

                            "category": get_category(file),

                            "size": round(
                                file.stat().st_size / 1024,
                                2
                            )

                        }

                    )


                except PermissionError:

                    continue



    return scanned_files