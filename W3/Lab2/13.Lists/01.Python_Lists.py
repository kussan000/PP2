#1.List

"""
Lists are used to store multiple items in a single variable.

Lists are created using square brackets:

"""

#Example 1
mylist = ["a", "b", "c"]
print(mylist)

#2.List Items

"""
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

"""

#3.Ordered

"""
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

"""
#4.Changeable

"""
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

"""

#5.Allow Duplicates

"""
Since lists are indexed, lists can have items with the same value:

"""

#Example 1
mylistlist = ["a", "b", "c", "a", "c"]
print(mylist)

#6.List Length

#To determine how many items a list has, use the len() function:

#Example  1
mylistlist = ["a", "b", "c"]
print(len(mylist))

#7.List Items - Data Types

#List items can be of any data type:

#Example 1
list1 = ["apple", "banana", "cherry"] # str
list2 = [1, 5, 7, 9, 3]               # int
list3 = [True, False, False]          # bool

#A list can contain different data types:

#Example 2
list1 = ["abc", 34, True, 40, "male"] # str, int, bool

#8.type()

#From Python's perspective, lists are defined as objects with the data type 'list':

#Example 1
mylist = ["a", "b", "c"]
print(type(mylist)) # <class 'list'>

#9.The list() Constructor

#It is also possible to use the list() constructor when creating a new list.

#Example 1
list1 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(list1)

#10.Python Collections (Arrays)

"""
There are four collection data types in the Python programming language:

    List            is a collection which is ordered and changeable.                    Allows duplicate members.
    Tuple           is a collection which is ordered and unchangeable.                  Allows duplicate members.
    Set             is a collection which is unordered, unchangeable*, and unindexed.   No duplicate members.
    Dictionary      is a collection which is ordered** and changeable.                  No duplicate members.

"""