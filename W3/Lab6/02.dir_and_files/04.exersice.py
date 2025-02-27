import os
import string

with open("W3/Lab6/02.dir_and_files/04.example_file.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()