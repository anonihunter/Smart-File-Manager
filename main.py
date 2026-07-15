from pathlib import Path
import shutil

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
    
    for file in directory.iterdir():
        for exten in extension_type:
            if exten in file.name and Path(directory/extension_type[exten]).exists():
                shutil.move(file, directory/extension_type[exten])
                index += 1
            else:
                Path(directory/extension_type[exten]).mkdir(parents=True, exist_ok=True)
    
    return f"No of operations: {index}"
            
        
print(classify_file(p))