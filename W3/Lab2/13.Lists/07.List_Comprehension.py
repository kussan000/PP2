#1.List Comprehension

#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Example 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:

#Example 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#2.The Syntax

#newlist = [expression for item in iterable if condition == True]

#Example 1
newlist = [x for x in fruits if x != "apple"]

#The condition is optional and can be omitted:

#Example 2
newlist = [x for x in fruits]

#3.Iterable

#The iterable can be any iterable object, like a list, tuple, set etc.

#Example 1
newlist = [x for x in range(10)]

#4.Expression

#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

#Example 1
newlist = [x.upper() for x in fruits]

#Example 2
newlist = ['hello' for x in fruits]

#Example 3
newlist = [x if x != "banana" else "orange" for x in fruits]