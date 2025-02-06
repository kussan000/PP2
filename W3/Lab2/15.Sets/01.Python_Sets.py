#1.Set

"""
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

"""

#Example 1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2.Set Items
 
#Set items are unordered, unchangeable, and do not allow duplicate values.

#3.Unordered

"""
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

"""

#4.Unchangeable

"""
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

"""

#5.Duplicates Not Allowed

#Duplicates Not Allowed

#Example 1
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) # {'banana', 'cherry', 'apple'}

#The values True and 1 are considered the same value in sets, and are treated as duplicates:

#Example 2
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset) # {True, 2, 'banana', 'cherry', 'apple'}

#The values False and 0 are considered the same value in sets, and are treated as duplicates:

#Example 3
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset) # {True, 2, 'banana', 'cherry', 'apple'}

#6.Get the Length of a Set

#To determine how many items a set has, use the len() function.

#Example 1
thisset = {"apple", "banana", "cherry"}

print(len(thisset)) # 3

#7.Set Items - Data Types

#Set items can be of any data type:

#Example 1
set1 = {"apple", "banana", "cherry"} # str
set2 = {1, 5, 7, 9, 3}               # int
set3 = {True, False, False}          # bool

#A set can contain different data types:

#Example 2
set1 = {"abc", 34, True, 40, "male"} # str, int, bool

#8.type()

#From Python's perspective, sets are defined as objects with the data type 'set':

#Example 1
myset = {"apple", "banana", "cherry"}
print(type(myset)) # <class 'set'>

#9.The set() Constructor

#It is also possible to use the set() constructor to make a set.

#Example 1
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#10.Python Collections (Arrays)

"""
There are four collection data types in the Python programming language:

    List            is a collection which is ordered and changeable. Allows duplicate members.
    Tuple           is a collection which is ordered and unchangeable. Allows duplicate members.
    Set             is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary      is a collection which is ordered** and changeable. No duplicate members.

"""

