#1.Access Items

"""
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

"""

#Example 1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

#Example 2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Example 3
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#2.Change Items

#Once a set is created, you cannot change its items, but you can add new items.
