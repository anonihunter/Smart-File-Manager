from pathlib import Path
import shutil
import hashlib
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configure the core logging settings
logging.basicConfig( 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s", 
    datefmt='%Y-%m-%d %H:%M:%S')

# Create a named logger for this module
logger = logging.getLogger(__name__)


p = Path('C:\\Python Projects\\Files') #input the file directory where you want to organize like 'Path\\to\\directory'

def classify_file(directory): #fucntion for Docs Categorization same idea for another folders and things it take input and directory where we have to arrange

    logger.debug(f'Function Started with Path: {directory}')

    count = 0

    extension_type = {'.pdf': 'Docs',
                    '.txt': 'Docs',
                    '.docx': 'Docs',
                    '.bmp': 'Images',
                    '.jpeg': 'Images',
                    '.jpg': 'Images',
                    '.png': 'Images',
                    '.mp4': 'Videos',
                    '.mkv': 'Videos',
                    '.mp3': 'Audio',
                    '.m4a': 'Audio',
                    '.zip': 'Zip File'
                      }
    
    keys_lst = list(extension_type)
    for file in directory.iterdir():
        for exten in keys_lst:
            if Path(directory/extension_type[exten]).exists():
                if exten in file.name:
                    shutil.move(file, directory/extension_type[exten])
                    logger.info(f'File, {file.name} Moved To: {directory/extension_type[exten]}')
                    count += 1

            else:
                Path(directory/extension_type[exten]).mkdir(parents=True, exist_ok=True)
                logger.info(f'Directory Created: {directory/extension_type[exten]}')
    
    return f"No of operations: {count}, File Transferred"            
        
# print(classify_file(p))


# def hashFile(filepath):
#     with open(filepath, 'rb') as file:
#         digest = hashlib.file_digest(file, 'sha256')
#         logger.info(f'File, {filepath.name} is hashed')

#     return digest.hexdigest()

# def duplicateFile(directory):

#     index = 0

#     file_hash = {}
#     duplicate = []
#     system_folder = ['Duplicate']

#     for file in directory.iterdir():
#         if file.is_dir() and file.name in system_folder:
#             continue
#         for items in file.iterdir():
#             if Path(directory/'Duplicate').exists():
#                 if (hashFile(items) in file_hash and 'Copy' in items.name):
#                     shutil.move(items, directory/'Duplicate')
#                     duplicate.append(items)
#                     index += 1
#                     logger.info(f'Duplicate File {items} Found & moved to {directory/'Duplicate'}')
#             else:
#                 Path(directory/'Duplicate').mkdir(parents=True, exist_ok=True)            
#                 file_hash[hashFile(items)] = items.name
#                 logger.info(f'Folder for Duplicate File Created')

#     return f"No of Duplicates Found {index}, and Tranferred"


# print(duplicateFile(p))

class fileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            logging.info(f"New File Detected: {event.src_path}")
            classify_file(p)


if __name__ == '__main__':
    event_handler = fileHandler()
    observer = Observer()
    observer.schedule(event_handler, p, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()
