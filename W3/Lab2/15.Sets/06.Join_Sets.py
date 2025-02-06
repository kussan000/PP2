#1.Join Sets

"""
There are several ways to join two or more sets in Python.

    The union() and update() methods joins all items from both sets.

    The intersection() method keeps ONLY the duplicates.

    The difference() method keeps the items from the first set that are not in the other set(s).

    The symmetric_difference() method keeps all items EXCEPT the duplicates.

"""

#2.Union

#The union() method returns a new set with all items from both sets.

#Example 1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) # {'a', 'c', 1, 'b', 2, 3}

#You can use the | operator instead of the union() method, and you will get the same result.

#Example 2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) # {'a', 'c', 1, 'b', 2, 3}

#3.Join Multiple Sets

"""
All the joining methods and operators can be used to join multiple sets.

When using a method, just add more sets in the parentheses, separated by commas:

"""

#Example 1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) # {banana, 2, 3, John, Elena, cherry, 'a', 1, 'c', apple, 'b'}

#When using the | operator, separate the sets with more | operators:

#Example 2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#4.Join a Set and a Tuple

"""
The union() method allows you to join a set with other data types, like lists or tuples.

The result will be a set.

"""

#Example 1
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y) #The | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
print(z) # {'b', 1, 'a', 'c', 2, 3}

#5.Update

"""
The update() method inserts all items from one set into another.

The update() changes the original set, and does not return a new set.

"""

#Example 1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) # {1, 'c', 'a', 2, 'b', 3}

#Both union() and update() will exclude any duplicate items.

#6.Intersection

"""
Keep ONLY the duplicates

The intersection() method will return a new set, that only contains the items that are present in both sets.

"""

#Example 1
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) # {'apple'}

#You can use the & operator instead of the intersection() method, and you will get the same result.

#Example 2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) # {'apple'}

#The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

#Example 3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1) # {'apple'}

#The values True and 1 are considered the same value. The same goes for False and 0.

#Example 4
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3) # {False, True, 'apple'}

#7.Difference

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

#Example 1
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3) # {'banana', 'cherry'}

#You can use the - operator instead of the difference() method, and you will get the same result.

#Example 2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3) # {'banana', 'cherry'}

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

#Example 3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1) # {'banana', 'cherry'}

#8.Symmetric Differences

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.

#Example 1
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) # {'google', 'banana', 'microsoft', 'cherry'}

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

#Example 2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3) # {'google', 'banana', 'microsoft', 'cherry'}

#The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

#Example 3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1) # {'google', 'banana', 'microsoft', 'cherry'}