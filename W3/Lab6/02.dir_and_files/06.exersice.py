import string

def create_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(f"W3/Lab6/02.dir_and_files/06.example_file/{filename}", 'w') as file:
            file.write("Hello world!")

create_files()