#1.Loop Through a List

#You can loop through the list items by using a for loop:

#Example 1
mylist = ["a", "b", "c"]
for i in mylist:
    print(i)

#2.Loop Through the Index Numbers

"""
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

"""

#Example 2
mylist = ["a", "b", "c"]
for i in range(len(mylist)):
    print(mylist[i])

#3.Using a While Loop

"""
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.

"""

mylist = ["a", "b", "c"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1

#4.Looping Using List Comprehension

#List Comprehension offers the shortest syntax for looping through lists:

#Example 1
mylist = ["a", "b", "c"]
[print(i) for i in mylist]