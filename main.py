from collections import Counter, defaultdict
from pathlib import Path


from scanner import scan_folders
from organizer import organize_files


from cleanup import (
    analyze_files,
    delete_files,
    cleanup_report
)


from notification import show_notification


from config import SCAN_FOLDERS





# =====================================
# PREVIEW
# =====================================

def show_preview(files):

    preview = defaultdict(list)


    for file in files:

        preview[file["category"]].append(file)



    print("\n")
    print("=" * 70)
    print("                 PREVIEW MODE")
    print("=" * 70)



    total = 0



    for category in sorted(preview):


        print(f"\n📂 {category}")
        print("-" * 50)



        for file in preview[category][:5]:

            print(
                "•",
                file["name"]
            )



        if len(preview[category]) > 5:

            print(
                f"...and {len(preview[category])-5} more"
            )



        total += len(preview[category])



    print("\n" + "=" * 70)

    print(
        f"Total files : {total}"
    )

    print("=" * 70)







# =====================================
# ORGANIZER
# =====================================

def run_organizer(files):


    desktop = (

        Path.home()
        /
        "OneDrive"
        /
        "Desktop"

    )



    destination = (

        desktop
        /
        "Organized_Files"

    )



    destination.mkdir(

        parents=True,
        exist_ok=True

    )



    print("\nDestination:")
    print(destination)



    try:


        moved, skipped = organize_files(

            files,
            destination

        )



        print("\n")
        print("=" * 70)
        print("       ORGANIZATION COMPLETE")
        print("=" * 70)



        print(
            f"Moved   : {moved}"
        )


        print(
            f"Skipped : {skipped}"
        )



    except Exception as e:


        print(
            "\nOrganizer Error:",
            e
        )








# =====================================
# CLEANUP
# =====================================

def run_cleanup():


    print("\n")
    print("=" * 70)
    print("             AI CLEANUP ASSISTANT")
    print("=" * 70)



    result = analyze_files(

        SCAN_FOLDERS

    )



    cleanup_report(

        result

    )



    safe = result["safe_delete"]



    if not safe:


        print(
            "\nNo safe cleanup required."
        )

        return





    show_notification(

        "AI Cleanup Assistant",

        f"{len(safe)} temporary files found"

    )





    choice = input(

        "\nMove safe junk files to Recycle Bin? (Y/N): "

    ).lower().strip()





    if choice == "y":



        deleted = delete_files(

            safe

        )



        print(

            f"\nMoved to Recycle Bin : {deleted}"

        )



    else:


        print(

            "\nCleanup skipped."

        )









# =====================================
# UNKNOWN EXTENSIONS
# =====================================

def show_unknown(files):


    unknown = Counter()



    for file in files:


        if file["category"] == "Others":


            ext = Path(
                file["name"]
            ).suffix.lower()



            if ext == "":

                ext = "[No Extension]"



            unknown[ext] += 1





    print("\n")
    print("=" * 70)
    print("UNKNOWN EXTENSIONS")
    print("=" * 70)



    for ext,count in unknown.most_common(20):

        print(
            f"{ext:<15} {count}"
        )









# =====================================
# MAIN
# =====================================

def main():


    print("=" * 70)

    print(
        "              AI FILE ORGANIZER"
    )

    print("=" * 70)




    # Scan

    files = scan_folders()



    if not files:


        print(
            "\nNo files found."
        )

        return





    print(

        f"\nTotal Files Found : {len(files)}"

    )




    # Category Summary


    counter = Counter(

        file["category"]

        for file in files

    )



    print("\nCategory Summary")

    print("-" * 70)



    for category,count in sorted(counter.items()):


        print(

            f"{category:<15}:{count}"

        )





    show_unknown(files)



    show_preview(files)






    # Organizer


    choice = input(

        "\nOrganize files now? (Y/N): "

    ).lower().strip()



    if choice == "y":


        run_organizer(files)



    else:


        print(

            "\nOrganization cancelled."

        )






    # Cleanup AFTER organizing


    run_cleanup()







if __name__ == "__main__":

    main()