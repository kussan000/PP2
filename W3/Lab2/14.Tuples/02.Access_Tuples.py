#1.Access Tuple Items

#You can access tuple items by referring to the index number, inside square brackets:

#Example 1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # "banana"

#2.Negative Indexing

"""
Negative indexing means start from the end.

-1 refers to the last item, -2 refers to the second last item etc.

"""

#Example 1
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # "cherry"

#3.Range of Indexes

"""
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.

"""

#Example 1
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # "cherry", "orange", "kiwi"

#By leaving out the start value, the range will start at the first item:

#Example 2
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) # "apple", "banana", "cherry", "orange"

#By leaving out the end value, the range will go on to the end of the tuple:

#Example 3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) # "cherry", "orange", "kiwi", "melon", "mango"

#4.Range of Negative Indexes

#Specify negative indexes if you want to start the search from the end of the tuple:

#Example 1
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # "orange", "kiwi", "melon"

#5.Check if Item Exists

#To determine if a specified item is present in a tuple use the in keyword:

#Example 1
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple: # check with keyword 'in'
    print("Yes, 'apple' is in the fruits tuple")

