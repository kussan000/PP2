#1.Change Item Value

#To change the value of a specific item, refer to the index number:

#Example 1
mylist = ["a", "b", "c"]
mylist[1] = "d"
print(mylist) # ["a", "d", "c"]

#2.Change a Range of Item Values

#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

#Example 1
mylist = ["a", "b", "c", "d", "e", "f"]
mylist[0:2] = ["g", "h"]
print(mylist) # ["g", "h", "c", "d", "e", "f"]

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

#Exanple 2
mylist = ["a", "b", "c"]
mylist[1:2] = ["d", "e"]
print(mylist) # ["a", "d", "e", "c"]

#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

#Example 3
mylist = ["a", "b", "c"]
mylist[1:3] = ["d"]
print(mylist) # ["d", "c"]

#3.Insert Items
"""
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

"""

#Example 1
mylist = ["a", "b", "c"]
mylist.insert(2, "d")
print(mylist) # ["a", "d", "c"]