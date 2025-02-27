#1.Join Two Lists

"""
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

"""

#Example 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) # ["a", "b", "c", 1, 2, 3]

#Another way to join two lists is by appending all the items from list2 into list1, one by one:

#Example 2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) # ["a", "b", "c", 1, 2, 3]

#Or you can use the extend() method, where the purpose is to add elements from one list to another list:

#Example 3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) # ["a", "b", "c", 1, 2, 3]