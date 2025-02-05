#1.Append Items

#To add an item to the end of the list, use the append() method:

#Example 1
mylist = ["a", "b", "c"]
mylist.append("d")
print(mylist) # ["a", "b", "c", "d"]

#2.Insert Items

"""
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:

"""

#Example 1
mylist = ["a", "b", "c"]
mylist.insert(1, "o")
print(mylist) # ["a", "d", "c"]

#3.Extend List

#To append elements from another list to the current list, use the extend() method.

#Example 3
mylist = ["a", "b", "c"]
yourlist = ["d", "e", "f"]
mylist.extend(yourlist)
print(mylist) # ["a", "b", "c", "d", "e", "f"]

#4.Add Any Iterable

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

mylist = ["a", "b", "c"]
yourtuple = ("d", "e")
mylist.extend(yourtuple)
print(mylist) # ["a", "b", "c", "d", "e"]

