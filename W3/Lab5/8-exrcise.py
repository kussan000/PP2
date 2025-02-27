import re 


with open("W3/Lab5/row-8-exercise.txt") as f:
    data = f.read()
    
print("Task 8")

print(re.findall(r"[A-Z][^A-Z]*", data))
