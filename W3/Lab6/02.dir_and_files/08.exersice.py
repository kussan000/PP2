import os
def delete(path_file):
    if os.path.exists(path_file):
        if os.access(path_file,os.W_OK):
            try:
                os.remove(path_file)
                print(f"file {path_file} delete") 
            except Exception as e:
                print("Error")
                
                
        else:
            print("You do not have write access")
    else:
        print(f"File '{path_file}' does not exist.")
            
        


path_delete = "W3/Lab6/02.dir_and_files/08.example_file.txt"

delete(path_delete)
