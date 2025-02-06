#1.Python Loops

"""
Python has two primitive loop commands:

    while loops
    for loops

"""

#2.The while Loop

#With the while loop we can execute a set of statements as long as a condition is true.

#Example 1
i = 1
while i < 6:
    print(i)
    i += 1

#The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

#3.The break Statement

#With the break statement we can stop the loop even if the while condition is true:

#Example 1
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#4.The continue Statement

#With the continue statement we can stop the current iteration, and continue with the next:

#Example 1
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#5.The else Statement

#With the else statement we can run a block of code once when the condition no longer is true:

#Example 1
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

