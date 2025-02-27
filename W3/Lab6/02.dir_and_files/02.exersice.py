import os

def check(path):
    if not os.path.exists(path):
        print("path doesn't exist")
    else:
        print('path does exist')
        if os.access(path, os.R_OK):
            print("readable")
        else:
            print("don't readable")
        if os.access(path, os.W_OK):
            print("writable")
        else:
            print("don't writable")
        if os.access(path, os.X_OK):
            print("executable")
        else:
            print("don't executable")

path_to_check = r"W3/Lab6/02.dir_and_files"
    
check(path_to_check)