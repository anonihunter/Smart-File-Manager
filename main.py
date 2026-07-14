from pathlib import Path
import shutil

p = Path('C:\\Python Projects\\Files')

def classify_file(directory): #function for Docs Categorization same idea for another folders and things it take input and directory where we have to arrange

    docs = ['.txt', '.pdf', '.docx']
    index = 0
    for file in directory.iterdir():
        for extension in docs:
            if extension in file.name and Path(directory/'Docs').exists():
                shutil.move(file, directory/'Docs')
                index = index + 1
            else:
                Path(directory/'Docs').mkdir(parents=True, exist_ok=True)
    
    return index
            

print(classify_file(p))