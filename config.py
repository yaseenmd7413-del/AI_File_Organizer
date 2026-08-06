from pathlib import Path


# =====================================
# APP INFO
# =====================================

APP_NAME = "AI File Organizer"
VERSION = "1.0.0"



# =====================================
# PROJECT PATHS
# =====================================

BASE_DIR = Path(__file__).resolve().parent


BACKUP_DIR = BASE_DIR / "backup"
LOGS_DIR = BASE_DIR / "logs"
REPORT_DIR = BASE_DIR / "report"
ASSETS_DIR = BASE_DIR / "assets"



# =====================================
# WINDOWS PATHS
# =====================================

HOME_DIR = Path.home()

ONEDRIVE_DIR = HOME_DIR / "OneDrive"


DESKTOP_DIR = ONEDRIVE_DIR / "Desktop"
DOWNLOADS_DIR = ONEDRIVE_DIR / "Downloads"

DOCUMENTS_DIR = ONEDRIVE_DIR / "Documents"
PICTURES_DIR = ONEDRIVE_DIR / "Pictures"
VIDEOS_DIR = ONEDRIVE_DIR / "Videos"
MUSIC_DIR = ONEDRIVE_DIR / "Music"



# =====================================
# SCAN FOLDERS
# =====================================

SCAN_FOLDERS = [

    DESKTOP_DIR,
    DOWNLOADS_DIR,
    DOCUMENTS_DIR,
    PICTURES_DIR,
    VIDEOS_DIR,
    MUSIC_DIR

]


# =====================================
# IGNORE FOLDERS
# =====================================

IGNORE_FOLDERS = [

    "venv",
    ".venv",
    "__pycache__",

    ".git",
    ".vscode",
    ".idea",

    "node_modules",

    "backup",
    "logs",
    "report",
    "assets",

    "AI_File_Organizer",
    "Organized_Files"

]



# =====================================
# IGNORE FILES
# =====================================

IGNORE_FILES = [

    ".gitignore",
    ".gitkeep",
    "desktop.ini"

]



# =====================================
# SAFETY
# =====================================


# First always keep True
# False only when ready

DRY_RUN = True



# Backup before moving

CREATE_BACKUP = True



# Duplicate handling

MOVE_DUPLICATES = False



# =====================================
# CATEGORY FOLDERS
# =====================================

CATEGORY_FOLDERS = {


    "Images":
        "Images",


    "Videos":
        "Videos",


    "Music":
        "Music",


    "Documents":
        "Documents",


    "Spreadsheets":
        "Spreadsheets",


    "Presentations":
        "Presentations",


    "Archives":
        "Archives",


    "Programs":
        "Programs",


    "Code":
        "Code",


    "Fonts":
        "Fonts",


    "Design":
        "Design",


    "Database":
        "Database",


    "Torrent":
        "Torrent",


    "Others":
        "Others"

}



# =====================================
# CREATE REQUIRED DIRECTORIES
# =====================================

for folder in [

    BACKUP_DIR,
    LOGS_DIR,
    REPORT_DIR,
    ASSETS_DIR

]:

    folder.mkdir(
        parents=True,
        exist_ok=True
    )