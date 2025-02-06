#1.Python Conditions and If statements

"""
Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

"""

#Example 1
a = 33
b = 200
if b > a:
    print("b is greater than a")

#2.Indentation

#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
 
#Example 1
"""
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error

"""

#3.Elif

#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

#Example 1
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#3.Elif

#The else keyword catches anything which isn't caught by the preceding conditions.

#Example 1
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#You can also have an else without the elif:

#Example 2
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#4.Short Hand If

#If you have only one statement to execute, you can put it on the same line as the if statement.
 
#Example 1
if a > b: print("a is greater than b")

#5.Short Hand If ... Else

#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

#Example 1
a = 2
b = 330
print("A") if a > b else print("B")

#You can also have multiple else statements on the same line:

#Example 2
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#6.And

#The and keyword is a logical operator, and is used to combine conditional statements:

#Example 2
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

#7.Or

#The or keyword is a logical operator, and is used to combine conditional statements:
 
#Example 1
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

#8.Not

#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

#Example 1
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

#9.Nested If

#You can have if statements inside if statements, this is called nested if statements.

#Example 1
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#10.The pass Statement

#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

#Example 1
a = 33
b = 200

if b > a:
        pass