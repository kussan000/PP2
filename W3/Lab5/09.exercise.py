import re
with open("W3/Lab5/09.row_exercise.txt") as f:
    data=f.read()
print(re.findall(r"[A-Z][a-z]*", data))