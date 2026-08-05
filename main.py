from scanner import scan_folders


def main():

    files = scan_folders()

    print("=" * 70)
    print("        AI FILE ORGANIZER")
    print("=" * 70)

    print(f"\nTotal Files Found : {len(files)}\n")

    for file in files[:20]:

        print(
            f"[{file['category']}]  "
            f"{file['name']}  "
            f"({file['size']} KB)"
        )

    if len(files) > 20:
        print(f"\n...and {len(files)-20} more files.")


if __name__ == "__main__":
    main()