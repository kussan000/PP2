import re 


with open("W3/Lab5/10.row_exercise.txt") as f:
    data = f.read()

matches=re.sub(r"[A-Z]",'_',data)
print(matches)