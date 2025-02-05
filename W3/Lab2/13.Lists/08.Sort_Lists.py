#1.Sort List Alphanumerically

#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

#Example list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Example list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#2.Sort Descending

#To sort descending, use the keyword argument reverse = True:

#Example list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Example list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#3.Customize Sort Function

"""
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):

"""

#Example 1
def myfunc(n):
  return abs(n - 40)

thislist = [105, 53, 76, 14, 35]
thislist.sort(key = myfunc)
print(thislist) # Sort the list based on how close the number is to 40:

#4.Case Insensitive Sort

#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

#Example 1 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # ['Kiwi', 'Orange', 'banana', 'cherry']

"""
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

"""

#Example 2
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']

#5.Reverse Order

"""
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.

"""

#Example 1
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana']