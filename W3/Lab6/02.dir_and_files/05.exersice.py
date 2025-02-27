def file(strings):
    with open("W3/Lab6/02.dir_and_files/05.example_file.txt", '+a') as f:
        text = ""
        for i in strings:
            text += str(i)+' '
        f.write(text)
        f.close()
    
 

file([1, 2, 3, "dfdf", "gregf", True, False])