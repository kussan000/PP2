import re 


with open("W3/Lab5/08.row_exercise.txt") as f:
    data = f.read()
    
print("Task 8")

print(re.findall(r"[A-Z][^A-Z]*", data))
