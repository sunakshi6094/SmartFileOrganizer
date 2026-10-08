import argparse
import shutil
import sys
from pathlib import Path


FILE_CATEGORIES = {
    "Documents": {".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"},
    "PDFs": {".pdf"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov"},
    "Audio": {".mp3", ".wav", ".aac"},
    "Archives": {".zip", ".rar", ".7z"},
}


def get_category(file_path):
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_destination = destination.parent / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_folder(folder):
    folder = Path(folder)

    if not folder.exists():
        print(f"Error: The folder '{folder}' does not exist.")
        return False

    if not folder.is_dir():
        print(f"Error: '{folder}' is not a folder.")
        return False

    for file_path in folder.iterdir():
        if not file_path.is_file():
            continue

        category = get_category(file_path)
        category_folder = folder / category

        category_folder.mkdir(exist_ok=True)

        destination = category_folder / file_path.name
        destination = get_unique_destination(destination)

        shutil.move(str(file_path), str(destination))

        if destination.name == file_path.name:
            print(f"Moved: {file_path.name} -> {category}/")
        else:
            print(
                f"Moved: {file_path.name} -> "
                f"{category}/{destination.name} "
                f"(renamed to avoid duplicate)"
            )

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Smart File Organizer - Organize files safely by type."
    )

    parser.add_argument(
        "folder",
        help="Path of the folder whose files you want to organize"
    )

    args = parser.parse_args()

    success = organize_folder(args.folder)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        print("The organizer stopped safely.")
        sys.exit(130)