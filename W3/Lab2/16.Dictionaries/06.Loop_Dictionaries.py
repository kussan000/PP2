#1.Loop Through a Dictionary

"""
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

"""

#Example 1 # key
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)

#Example 2 # value
for x in thisdict:
    print(thisdict[x])

#Example 3 # value
for x in thisdict.values():
    print(x)

#Example 4 # key
for x in thisdict.keys():
    print(x)

#Example 5 # item
for x, y in thisdict.items():
    print(x, y)