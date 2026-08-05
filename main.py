from collections import Counter, defaultdict
import os

from scanner import scan_folders


def show_preview(files):
    preview = defaultdict(list)

    for file in files:
        preview[file["category"]].append(file)

    print("\n")
    print("=" * 70)
    print("                     PREVIEW MODE")
    print("=" * 70)

    total = 0

    for category in sorted(preview.keys()):
        print(f"\n📂 {category}")
        print("-" * 50)

        for f in preview[category][:5]:
            print(f"• {f['name']}")

        if len(preview[category]) > 5:
            print(f"...and {len(preview[category]) - 5} more")

        total += len(preview[category])

    print("\n" + "=" * 70)
    print(f"Total files to organize : {total}")
    print("=" * 70)


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

    # Unknown Extensions Report
    unknown = Counter()

    for file in files:
        if file["category"] == "Others":
            ext = os.path.splitext(file["name"])[1].lower()
            if not ext:
                ext = "[No Extension]"
            unknown[ext] += 1

    print("\n")
    print("=" * 70)
    print("Unknown File Extensions")
    print("=" * 70)

    if unknown:
        for ext, count in unknown.most_common(30):
            print(f"{ext:<15} {count}")
    else:
        print("No unknown file extensions found.")

    # Preview Mode
    show_preview(files)


if __name__ == "__main__":
    main()