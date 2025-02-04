#1.Global Variables

#Global variables can be used by everyone, both inside of functions and outside.

#Example 1
x = "World!"

def myfunc():
  print("Hello " + x)

myfunc()

#Example 2
x = "World!"

def myfunc():
  x = "Python!"
  print("Hello " + x)

myfunc()

print("Hello " + x)

#2.The global Keyword

#If you use the global keyword, the variable belongs to the global scope:

#Example 1
def myfunc():
  global x
  x = "World!"

myfunc()

print("Hello " + x)

#Example 2
x = "World!"

def myfunc():
  global x
  x = "Python!"

myfunc()

print("Hello " + x)

