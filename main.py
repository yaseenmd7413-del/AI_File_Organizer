from collections import Counter
from scanner import scan_folders


def main():
    files = scan_folders()

    print("=" * 70)
    print("                 AI FILE ORGANIZER")
    print("=" * 70)

    print(f"\nTotal Files Found : {len(files)}\n")

    # Category Summary
    counter = Counter(file["category"] for file in files)

    print("Category Summary")
    print("-" * 70)

    for category, count in sorted(counter.items()):
        print(f"{category:<15} : {count}")

    print("\n" + "-" * 70)
    print("First 20 Files")
    print("-" * 70)

    for file in files[:20]:
        print(
            f"[{file['category']}] "
            f"{file['name']} "
            f"({file['size']} KB)"
        )

    if len(files) > 20:
        print(f"\n...and {len(files)-20} more files.")


if __name__ == "__main__":
    main()