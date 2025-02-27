import re
with open("W3/Lab5/row-9-exercise.txt") as f:
    data=f.read()
print(re.findall(r"[A-Z][a-z]*", data))