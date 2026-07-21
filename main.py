from pathlib import Path
import shutil
import hashlib

p = Path('C:\\Python Projects\\Files') #input the file directory where you want to organize like 'Path\\to\\directory'

def classify_file(directory): #fucntion for Docs Categorization same idea for another folders and things it take input and directory where we have to arrange

    index = 0

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
            if exten in file.name and Path(directory/extension_type[exten]).exists():
                shutil.move(file, directory/extension_type[exten])
                index += 1
            else:
                Path(directory/extension_type[exten]).mkdir(parents=True, exist_ok=True)
    
    return f"No of File: {index}, Organized"
                    
print(classify_file(p))

## hashing the file

def hashFile(filepath):
    with open(filepath, 'rb') as file:
        digest = hashlib.file_digest(file, 'sha256')

    return digest.hexdigest()

## Finding Duplicate Files

def duplicateFile(directory):

    index = 0

    file_hash = {}
    duplicate = []
    system_folder = ['Duplicate']

    for file in directory.iterdir():
        if file.is_dir() and file.name in system_folder:
            continue
        for items in file.iterdir():
            if (hashFile(items) in file_hash or 'Copy' in items.name) and Path(directory/'Duplicate').exists():
                shutil.move(items, directory/'Duplicate')
                duplicate.append(items)
                index += 1
            else:
                Path(directory/'Duplicate').mkdir(parents=True, exist_ok=True)            
                file_hash[hashFile(items)] = items.name

    print('Duplicate Files: ', duplicate)
    return f"No of Duplicates Found {index}, and Tranferred"


print(duplicateFile(p))