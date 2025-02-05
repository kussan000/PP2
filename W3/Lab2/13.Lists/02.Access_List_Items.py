#1.Access Items

#List items are indexed and you can access them by referring to the index number:

#Example 1
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # second value

#2.Negative Indexing

"""
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

"""

#Example 1
mylist = ["a", "b", "c"]
print(mylist[-1]) # last value

#3.Range of Indexes

"""
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

"""

#Example 1
mylist = ["a", "b", "c", "d", "e", "f", "g"]
print(mylist[1:6]) # ["b", "c", "d", "e", "f"]

#By leaving out the start value, the range will start at the first item:

#Example 2
mylist = ["a", "b", "c", "d", "e", "f", "g"]
print(mylist[:5]) # ["a", "b", "c", "d", "e"]

#By leaving out the end value, the range will go on to the end of the list:

#Example 2
mylist = ["a", "b", "c", "d", "e", "f", "g"]
print(mylist[3:]) # ["d", "e", "f", "g"]

#4.Range of Negative Indexes

#Specify negative indexes if you want to start the search from the end of the list:

#Example 1
mylist = ["a", "b", "c", "d", "e", "f", "g"]
print(mylist[-4:-2]) # ["d", "e"]

#5.Check if Item Exists

#To determine if a specified item is present in a list use the in keyword:

#Example 1
mylist = ["a", "b", "c"]
if "a" in mylist:
    print("Yes, 'a' is in the fruits list")