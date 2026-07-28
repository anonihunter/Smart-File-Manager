import hashlib
import shutil
from logger import logger
from pathlib import Path

def hashFile(filepath):
    with open(filepath, 'rb') as file:
        digest = hashlib.file_digest(file, 'sha256')
        logger.info(f'File, {filepath.name} is hashed')

    return digest.hexdigest()

def duplicateFile(directory):

    index = 0

    file_hash = {}
    directory = Path(directory)

    duplicate_folder = (directory/'Duplicate')
    duplicate_folder.mkdir(exist_ok=True)

    for file in directory.iterdir():
        if file.is_dir() and file.name is 'Duplicate':
            continue
        for items in file.iterdir():
            file_hash_val = hashFile(items)
            if (file_hash_val in file_hash or 'Copy' in items.name):
                shutil.move(items, duplicate_folder)
                index += 1
                logger.info(f'Duplicate File {items.name} Found & moved to {directory/'Duplicate'}')
            else:            
                file_hash_val = items.name

    return f"No of Duplicates Found {index}, and Tranferred" 