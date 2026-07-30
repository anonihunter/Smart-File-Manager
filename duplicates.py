import hashlib
import shutil
from stats import stats
from pathlib import Path
from config import config
from logger import logger

def hashFile(filepath):
    with open(filepath, 'rb') as file:
        digest = hashlib.file_digest(file, 'sha256')
        logger.info(f'File, {filepath.name} is hashed')

    return digest.hexdigest()

def duplicateFile(directory):

    duplicate_mode = config["duplicates"]["mode"]

    index = 0

    file_hash = {}
    directory = Path(directory)

    duplicate_folder = (directory/'Duplicate')
    duplicate_folder.mkdir(exist_ok=True)

    for file in directory.iterdir():
        if not file.is_dir():
            continue

        if file.name == 'Duplicate':
            continue

        for items in file.iterdir():
            file_hash_val = hashFile(items)
            if (file_hash_val in file_hash or 'Copy' in items.name):
                if duplicate_mode == "move":
                    shutil.move(items, duplicate_folder)
                    logger.info(f"Duplicate File {items.name} moved.")

                elif duplicate_mode == "skip":
                    logger.info(f"Duplicate File {items.name} skipped.")

                elif duplicate_mode == "report":
                    print(f"Duplicate Found : {items.name}")

                    index += 1
                    stats["duplicate_files"] += 1
            else:            
                file_hash_val = items.name

    return f"No of Duplicates Found {index}, and Tranferred" 