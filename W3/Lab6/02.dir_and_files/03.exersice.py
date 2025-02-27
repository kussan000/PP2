import os

path = r"W3/Lab6/02.dir_and_files"
def check(path):
    if os.path.exists(path):
        print("Name of file: ", os.path.basename(path))
        print("name of directory: ", os.path.dirname(path))
    else:
        print("This file does not exist(")
    
print(check(path))