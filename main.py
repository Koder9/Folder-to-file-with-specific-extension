import os
from easygui import diropenbox

def get_files():
    extension = input("What file extension do you want to find? (ex: .txt)")
    input("Press enter to load your folder to find your files.")
    path = diropenbox()
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if extension in file:
                files.append(os.path.join(r, file))
                with open("files.txt", "a") as f:
                    f.write(os.path.join(r, file))
    return files
    
get_files()
