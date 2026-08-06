from pathlib import Path


# =====================================
# PROTECTED EXTENSIONS
# =====================================

PROTECTED_EXTENSIONS = [

    ".py",
    ".js",
    ".java",
    ".cpp",
    ".c",
    ".html",
    ".css",

    ".pdf",
    ".docx",
    ".xlsx",
    ".pptx",

    ".json",
    ".xml",
    ".yaml",
    ".yml",

]


# =====================================
# PROTECTED FILE NAMES
# =====================================

PROTECTED_NAMES = [

    "readme.md",
    "requirements.txt",
    ".gitignore",
    "package.json",
    "config.py",
    "main.py"

]



# =====================================
# SAFE TEMP EXTENSIONS
# =====================================

TEMP_EXTENSIONS = [

    ".tmp",
    ".temp",
    ".opdownload",
    ".crdownload",
    ".part"

]



# =====================================
# SAFETY CHECK
# =====================================


def check_file_safety(file_path):

    path = Path(file_path)


    name = path.name.lower()

    ext = path.suffix.lower()



    # -------------------------
    # Protected names first
    # -------------------------

    if name in PROTECTED_NAMES:

        return {

            "action": "PROTECTED",

            "reason":
            "Important system/project file"

        }



    # -------------------------
    # Protected extensions
    # -------------------------

    if ext in PROTECTED_EXTENSIONS:

        return {

            "action": "PROTECTED",

            "reason":
            "Important file type"

        }



    # -------------------------
    # Temporary files
    # -------------------------

    if ext in TEMP_EXTENSIONS:


        return {

            "action":"SAFE_DELETE",

            "reason":
            "Temporary incomplete file"

        }



    if name.startswith("~"):


        return {

            "action":"SAFE_DELETE",

            "reason":
            "Temporary Office/cache file"

        }



    # -------------------------
    # Empty files
    # -------------------------

    try:

        if path.exists():

            size = path.stat().st_size


            if size == 0:

                return {

                    "action":"REVIEW",

                    "reason":
                    "Empty file"

                }


    except Exception:

        pass



    # -------------------------
    # Unknown
    # -------------------------

    return {

        "action":"REVIEW",

        "reason":
        "Unknown file"

    }