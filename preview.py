from collections import defaultdict

def show_preview(files):
    preview = defaultdict(list)

    for file in files:
        preview[file["category"]].append(file)

    print("\n" + "=" * 70)
    print("PREVIEW MODE")
    print("=" * 70)

    total = 0

    for category in sorted(preview.keys()):
        print(f"\n📂 {category}")
        print("-" * 50)

        for file in preview[category][:5]:
            print(file["name"])

        if len(preview[category]) > 5:
            print(f"...and {len(preview[category])-5} more")

        total += len(preview[category])

    print("\n" + "=" * 70)
    print(f"Total files to organize : {total}")
    print("=" * 70)