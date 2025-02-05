#1.Boolean Values

#Booleans represent one of two values: True or False.

#Example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Example 2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#2.Evaluate Values and Variables
 
#The bool() function allows you to evaluate any value, and give you True or False in return,

#Example 1
print(bool("Hello"))
print(bool(15))

#Example 2
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#3.Most Values are True

"""
    Almost any value is evaluated to True if it has some sort of content.
    Any string is True, except empty strings.
    Any number is True, except 0.
    Any list, tuple, set, and dictionary are True, except empty ones.
"""

#Example 1
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#4.Some Values are False

#In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

#Example 1 
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

#Example 2  
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#5.Functions can Return a Boolean

#You can create functions that returns a Boolean Value:

#Example 1
def myFunction() :
  return True

print(myFunction())

#Example 2
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Example 3
x = "a"
print(x.isdigit())