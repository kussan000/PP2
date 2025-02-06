#1.Remove Item

#To remove an item in a set, use the remove(), or the discard() method.

#Example 1
thisset = {"apple", "banana", "cherry"} 

thisset.remove("banana") # If the item to remove does not exist, remove() will raise an error.

print(thisset)

#Example 2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") # If the item to remove does not exist, discard() will NOT raise an error.

print(thisset)

"""
You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.

"""

#Example 3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop() # Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

print(x)

print(thisset)

#Example 4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset) # Empty

#Example 5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) # Error