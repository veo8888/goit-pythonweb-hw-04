"""
random_file_generator.py
Random File Structure Generator for Testing the Sorter

Functionality:
- creates random files with various extensions
- creates random folders with a specified nesting depth
- fills the files with random text

Run:
python random_file_generator.py
"""

import os
import random
import string


# Generating random file content
# ===============================
def random_text(length: int = 50) -> str:
    """
    Generates a string of random characters.
    """
    chars = string.ascii_letters + string.digits + " "
    return "".join(random.choices(chars, k=length))


# Creating a random file structure
# =================================
def create_random_structure(
    base_path: str, depth: int = 2, num_files: int = 5, num_folders: int = 3
) -> None:
    """
    Recursively creates folders and files.

    base_path   – the root directory
    depth       – the nesting depth
    num_files   – number of files at each level
    num_folders – number of folders at each level
    """

    if depth <= 0:
        return

    extensions = [
        ".txt",
        ".csv",
        ".pdf",
        ".doc",
        ".mp4",
        ".jpg",
        ".jpeg",
        ".png",
        ".mp3",
        ".xml",
    ]

    # Creating files
    for _ in range(num_files):
        filename = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        ext = random.choice(extensions)
        filepath = os.path.join(base_path, filename + ext)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(random_text())

    # Creating subfolders
    for _ in range(num_folders):
        subfolder = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        subpath = os.path.join(base_path, subfolder)

        os.makedirs(subpath, exist_ok=True)

        # Recursive creation of a level
        create_random_structure(
            subpath, depth=depth - 1, num_files=num_files, num_folders=num_folders
        )


# Entry point
# ============
def main():
    root = "random_structure"

    if not os.path.exists(root):
        os.makedirs(root)

    create_random_structure(root, depth=3, num_files=4, num_folders=2)
    print(f"\033[92m ✔ Structure created:\033[0m \033[4m {root}\033[0m")


if __name__ == "__main__":
    main()
