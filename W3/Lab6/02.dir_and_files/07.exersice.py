def copy():
    string = "W3/Lab6/02.dir_and_files/07.example_file_1.txt"

    with open(string) as file:
        data = file.read()
    file.close()

    with open("W3/Lab6/02.dir_and_files/07.example_file_2.txt", "+w") as file_copy:
        file_copy.write(data)
    file.close()

copy()