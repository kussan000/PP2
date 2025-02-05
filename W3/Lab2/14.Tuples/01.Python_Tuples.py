#1.Tuple 

"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

"""

#Example 1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#2.Tuple Items

"""
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

"""

#3.Ordered

#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

#4.Unchangeable

#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

#5.Allow Duplicates

#Since tuples are indexed, they can have items with the same value:

#Example 1
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#6.Tuple Length

#To determine how many items a tuple has, use the len() function:

#Example 1
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#7.Create Tuple With One Item

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

#Example 1
thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple)) # NOT a tuple

#8.Tuple Items - Data Types

#Tuple items can be of any data type:

#Example 1
tuple1 = ("apple", "banana", "cherry") # str
tuple2 = (1, 5, 7, 9, 3)               # int
tuple3 = (True, False, False)          # bool

#A tuple can contain different data types:

#Example 2
tuple1 = ("abc", 34, True, 40, "male") # str, int, bool

#9.type()

#From Python's perspective, tuples are defined as objects with the data type 'tuple':

#Example 1
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # <class 'tuple'>

#10.The tuple() Constructor

#It is also possible to use the tuple() constructor to make a tuple.

#Example 1
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#11.Python Collections (Arrays)

"""
There are four collection data types in the Python programming language:

    List            is a collection which is ordered and changeable. Allows duplicate members.
    Tuple           is a collection which is ordered and unchangeable. Allows duplicate members.
    Set             is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary      is a collection which is ordered** and changeable. No duplicate members.

"""

