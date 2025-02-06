#1.Nested Dictionaries

#A dictionary can contain dictionaries, this is called nested dictionaries.

#Example 1
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}

#Or, if you want to add three dictionaries into a new dictionary:

#Example 2
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

#2.Access Items in Nested Dictionaries

#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

#Example 1
print(myfamily["child2"]["name"])

#3.Loop Through Nested Dictionaries

#You can loop through a dictionary by using the items() method like this:

#Example 1
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

        