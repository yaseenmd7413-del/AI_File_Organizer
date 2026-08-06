from pathlib import Path
import shutil

from config import (
    CATEGORY_FOLDERS,
    BACKUP_DIR,
    CREATE_BACKUP,
    DRY_RUN
)



# =====================================
# Create Folder
# =====================================

def create_folder(path):

    path.mkdir(
        parents=True,
        exist_ok=True
    )



# =====================================
# Avoid Duplicate Names
# =====================================

def unique_name(destination):

    if not destination.exists():
        return destination


    counter = 1


    while True:

        new_name = (
            destination.stem
            + f"_{counter}"
            + destination.suffix
        )


        new_path = (
            destination.parent /
            new_name
        )


        if not new_path.exists():

            return new_path


        counter += 1




# =====================================
# Backup
# =====================================

def backup_file(file_path):

    if not CREATE_BACKUP:
        return


    create_folder(
        BACKUP_DIR
    )


    backup_path = (
        BACKUP_DIR /
        file_path.name
    )


    backup_path = unique_name(
        backup_path
    )


    shutil.copy2(
        file_path,
        backup_path
    )





# =====================================
# Main Organizer
# =====================================

def organize_files(files, destination):


    moved = 0
    skipped = 0


    destination = Path(
        destination
    )


    print("\n")
    print("=" * 70)
    print("                 ORGANIZER")
    print("=" * 70)



    for file in files:


        try:


            source = Path(
                file["path"]
            )


            if not source.exists():

                skipped += 1
                continue



            category = file["category"]



            if category not in CATEGORY_FOLDERS:

                category = "Others"



            # Category folder

            destination_folder = (

                destination /

                CATEGORY_FOLDERS[category]

            )



            create_folder(
                destination_folder
            )



            target = (

                destination_folder /

                source.name

            )



            target = unique_name(
                target
            )



            print(
                f"\n{source.name}"
            )

            print(
                f" → {target}"
            )



            # Preview only

            if DRY_RUN:

                print(
                    "[DRY RUN]"
                )

                continue



            # Backup

            backup_file(
                source
            )



            # Move

            shutil.move(
                str(source),
                str(target)
            )


            moved += 1



        except Exception as e:


            print(
                "ERROR:",
                e
            )

            skipped += 1




    

    print(
        f"Moved   : {moved}"
    )

    print(
        f"Skipped : {skipped}"
    )



    return moved, skipped