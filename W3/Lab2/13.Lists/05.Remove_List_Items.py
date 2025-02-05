#1.Remove Specified Item

#The remove() method removes the specified item.

#Example 1
mylist = ["a", "b", "c"]
mylist.remove("b")
print(mylist) # ["a", "c"]

#If there are more than one item with the specified value, the remove() method removes the first occurrence:

#Example 2
mylist = ["a", "b", "c", "b"]
mylist.remove("b")
print(mylist) # ["a", "c", "b"]

#2.Remove Specified Index

#The pop() method removes the specified index.

#Example 1 
mylist = ["a", "b", "c"]
mylist.pop(1)
print(mylist) # ["a", "c"]

#If you do not specify the index, the pop() method removes the last item.

#Example 2 
mylist = ["a", "b", "c"]
mylist.pop()
print(mylist) # ["a", "b"]

#The del keyword also removes the specified index:

#Example 3
mylist = ["a", "b", "c"]
del mylist[0]
print(mylist) # ["b", "c"]

#The del keyword can also delete the list completely.

#Example 4
mylist = ["a", "b", "c"]
del mylist # Empty

#3.Clear the List

"""
The clear() method empties the list.

The list still remains, but it has no content.

"""

#Example 1
mylist = ["a", "b", "c"]
mylist.clear()
print(mylist) # Empty