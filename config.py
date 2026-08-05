from pathlib import Path

# ==============================
# Project Information
# ==============================
APP_NAME = "AI File Organizer"
VERSION = "1.0.0"

# ==============================
# Project Paths
# ==============================
BASE_DIR = Path(__file__).resolve().parent

BACKUP_DIR = BASE_DIR / "backup"
LOGS_DIR = BASE_DIR / "logs"
REPORT_DIR = BASE_DIR / "report"
ASSETS_DIR = BASE_DIR / "assets"

# ==============================
# User Folders (Windows)
# ==============================
HOME_DIR = Path.home()

DESKTOP_DIR = HOME_DIR / "Desktop"
DOWNLOADS_DIR = HOME_DIR / "Downloads"
DOCUMENTS_DIR = HOME_DIR / "Documents"
PICTURES_DIR = HOME_DIR / "Pictures"
VIDEOS_DIR = HOME_DIR / "Videos"
MUSIC_DIR = HOME_DIR / "Music"

# ==============================
# Folders to Scan
# ==============================
SCAN_FOLDERS = [
    DESKTOP_DIR,
    DOWNLOADS_DIR,
]

# ==============================
# Safety
# ==============================
DRY_RUN = True      # True = Preview only
CREATE_BACKUP = True
MOVE_DUPLICATES = False

# ==============================
# Create Required Directories
# ==============================
for folder in [BACKUP_DIR, LOGS_DIR, REPORT_DIR]:
    folder.mkdir(exist_ok=True)