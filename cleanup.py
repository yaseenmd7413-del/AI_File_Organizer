from pathlib import Path
from send2trash import send2trash


TEMP_EXTENSIONS = [
    ".tmp",
    ".temp",
    ".opdownload",
    ".crdownload",
    ".part",
    ".cache"
]


PROTECTED_EXTENSIONS = [

    ".lnk",
    ".exe",
    ".msi",
    ".bat",
    ".cmd",

    ".py",
    ".java",
    ".cpp",
    ".c",
    ".js",

    ".pdf",
    ".doc",
    ".docx",

    ".jpg",
    ".jpeg",
    ".png",

    ".zip",
    ".rar"

]


PROTECTED_NAMES = [

    "README.md",
    "requirements.txt",
    ".gitkeep",
    "py.typed",
    "REQUESTED"

]



# =================================
# AI CLASSIFICATION
# =================================

def analyze_files(folders):


    result = {

        "safe_delete": [],
        "review": [],
        "protected": []

    }


    for folder in folders:


        for file in Path(folder).rglob("*"):


            try:

                if not file.is_file():
                    continue



                name = file.name.lower()
                ext = file.suffix.lower()



                # Protected names

                if name in [
                    x.lower()
                    for x in PROTECTED_NAMES
                ]:

                    result["protected"].append(file)
                    continue



                # Protected extension

                if ext in PROTECTED_EXTENSIONS:

                    result["protected"].append(file)
                    continue



                # Temporary files

                if ext in TEMP_EXTENSIONS:

                    result["safe_delete"].append(file)
                    continue



                # Empty files

                if file.stat().st_size == 0:


                    result["review"].append(file)



            except:

                pass



    return result




# =================================
# DELETE TO RECYCLE BIN
# =================================

def delete_files(files):


    deleted = 0


    for file in files:


        try:

            send2trash(
                str(file)
            )

            deleted += 1


        except Exception as e:

            print(
                "Error:",
                e
            )


    return deleted




# =================================
# REPORT
# =================================

def cleanup_report(result):


    print("\n")
    print("="*70)
    print("              AI CLEANUP REPORT")
    print("="*70)



    print(
        f"Safe Delete : {len(result['safe_delete'])}"
    )


    print(
        f"Review      : {len(result['review'])}"
    )


    print(
        f"Protected   : {len(result['protected'])}"
    )


    print("-"*70)



    for file in result["safe_delete"][:10]:

        print(
            "[DELETE]",
            file.name
        )



    print("="*70)