"""
sorted.py
Asynchronous File Sorter by File Extension

Functionality:
- recursively walks through the source directory
- creates a subfolder for each file based on its extension
- copies files asynchronously
- limits the number of concurrent operations (Semaphore)
- logs errors

Run:
python sorter.py "source_path" "output_path"
"""

import argparse
import asyncio
import logging
from pathlib import Path
import aiofiles
import aiofiles.os

# Statistics counters
files_copied = 0
files_failed = 0

# Logging configuration
logging.basicConfig(
    level=logging.ERROR,
    format="\033[41m %(asctime)s \033[0m - \033[4m %(levelname)s \033[0m - %(message)s",
)

# Limit on the number of files being copied concurrently
SEMAPHORE = asyncio.Semaphore(100)


# Asynchronous copying of a single file
# ======================================
async def copy_file(src: Path, dst_folder: Path) -> None:
    global files_copied, files_failed
    """
    Copies a single file into the subfolder corresponding to its extension.
    Uses streamed copying with semaphore-based concurrency limiting.
    """
    async with SEMAPHORE:
        try:
            # Determine the file extension
            ext = src.suffix.lower().lstrip(".") or "no_ext"
            target_dir = dst_folder / ext

            # Create a folder for the extension
            await aiofiles.os.makedirs(target_dir, exist_ok=True)

            target_file = target_dir / src.name

            # Chunk-based copying
            async with (
                aiofiles.open(src, "rb") as f_src,
                aiofiles.open(target_file, "wb") as f_dst,
            ):
                while chunk := await f_src.read(64 * 1024):  # 64 KiB
                    await f_dst.write(chunk)

            files_copied += 1  # Success count

        except Exception as e:
            files_failed += 1  # Error count
            logging.error(f"\033[91m Copy error {src}\033[0m: {e}")


# Asynchronous directory traversal
# =================================
async def process_folder(src_folder: Path, dst_folder: Path) -> None:
    """
    Recursively walks through the directory and creates copy tasks for each file.
    """
    tasks = [
        asyncio.create_task(copy_file(path, dst_folder))
        for path in src_folder.rglob("*")
        if path.is_file()
    ]

    await asyncio.gather(*tasks)


# Argument parser
# ================
def parse_args():
    parser = argparse.ArgumentParser(description="Async File Sorter")
    parser.add_argument("source", type=str, help="Source folder")
    parser.add_argument("output", type=str, help="Destination folder")
    return parser.parse_args()


# Entry point
# ============
async def main() -> None:
    """
    Main logic:
    - parse arguments
    - validate that the source directory exists
    - create the output directory
    - start the sorting process
    """
    args = parse_args()
    src_folder = Path(args.source)
    dst_folder = Path(args.output)

    if not src_folder.exists():
        logging.error(f"Source folder does not exist: {src_folder}")
        return

    dst_folder.mkdir(parents=True, exist_ok=True)

    await process_folder(src_folder, dst_folder)

    total = files_copied + files_failed
    files_skipped = 0

    # Final message
    # ==============
    print(
        f"\033[92m✔ File sorting completed successfully! \033[0m \033[42m File path-> \033[0m \033[4m {dst_folder}\033[0m"
    )
    print(f"📄 Files copied: {files_copied}")
    print(f"⛔ Errors: {files_failed}")
    print(f"🚫 Skipped: {files_skipped}")
    print(f"📦 Total processed: {total}")


if __name__ == "__main__":
    asyncio.run(main())
