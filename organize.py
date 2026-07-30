import shutil
from stats import stats
from pathlib import Path
from logger import logger
from config import config

def classify_file(directory): #fucntion for Docs Categorization same idea for another folders and things it take input and directory where we have to arrange

    logger.info(f'Function Started with Path: {directory}')

    count = 0

    extension_type = config["extension_mapping"]

    directory = Path(directory)
    
    keys_lst = list(extension_type)
    for file in directory.iterdir():
        if file.is_file():
            stats["files_scanned"] += 1
        for exten in keys_lst:
            if Path(directory/extension_type[exten]).exists():
                if file.suffix.lower() == exten:
                    shutil.move(file, directory/extension_type[exten])
                    stats["files_organized"] += 1
                    stats["category"][extension_type[exten]] += 1
                    logger.info(f'File, {file.name} Moved To: {directory/extension_type[exten]}')
                    count += 1

            else:
                Path(directory/extension_type[exten]).mkdir(parents=True, exist_ok=True)
                stats["folders_created"] += 1
                logger.info(f'Directory Created: {directory/extension_type[exten]}')

        stats["category"]["Others"] += 1
        stats["files_skipped"] += 1
    
    return f"No of operations: {count}, File Transferred"