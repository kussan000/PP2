#1.Change Tuple Values

"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

"""

#Example 1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) # "apple", "kiwi", "cherry"

#2.Add Items
 
#Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

#Example 1
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) # "apple", "banana", "cherry", "orange"

#Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

#Example 2
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) # "apple", "banana", "cherry", "orange"

#3.Remove Items

#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

#Eaxmple 1
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) # "banana", "cherry"

#Or you can delete the tuple completely:

#Example 2
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) # Empty
