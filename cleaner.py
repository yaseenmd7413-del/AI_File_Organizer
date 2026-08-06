from pathlib import Path


# =====================================
# Junk Detection Rules
# =====================================


TEMP_EXTENSIONS = [

    ".tmp",
    ".temp",
    ".opdownload",
    ".crdownload",
    ".part"

]


EMPTY_FILE_SIZE = 0




# =====================================
# Detect Junk Type
# =====================================


def detect_junk(file):


    name = file["name"]

    path = Path(
        file["path"]
    )


    extension = path.suffix.lower()



    # Temporary files

    if extension in TEMP_EXTENSIONS:

        return "Temporary File"



    # Empty files

    if file["size"] == EMPTY_FILE_SIZE:

        return "Empty File"



    # Windows temp files

    if name.startswith("~"):

        return "Temporary File"



    return None






# =====================================
# Cleanup Report
# =====================================


def cleanup_report(files):


    junk=[]



    for file in files:


        result = detect_junk(file)



        if result:


            junk.append(

                (
                    file,
                    result
                )

            )





    print("\n")

    print("="*70)

    print(
        "              AI CLEANUP REPORT"
    )

    print("="*70)





    if not junk:


        print(
            "No junk files detected."
        )



    else:


        for file,reason in junk:


            print(

                f"[{reason}] {file['name']}"

            )




        print("-"*70)

        print(

            f"Total Junk Files : {len(junk)}"

        )




    print("="*70)





    return junk