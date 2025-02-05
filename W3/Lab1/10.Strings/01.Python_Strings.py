#1.Strings

#Strings in python are surrounded by either single quotation marks, or double quotation marks.

#Example 1
print("Hello")
print('Hello')

#2.Quotes Inside Quotes

#Example 1
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#3.Assign String to a Variable

#Example 1
a = "Hello"
print(a)

#4.Multiline Strings

#Example 1
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Example 2
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#5.Strings are Arrays

#You must represent each character as an element of an array.

#Example 1
a = "Hello, World!"
print(a[1])

#6.Looping Through a String

#Since strings are arrays, we can loop through the characters in a string, with a for loop.

#Example 1
for x in "Apple":
    print(x)

#7.Check String

#To check if a certain phrase or character is present in a string, we can use the keyword in.

#Example with print
txt = "The best things in life are free!"
print("free" in txt)

#Example with if
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#8.Check if NOT

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

#Example with print
txt = "The best things in life are free!"
print("expensive" not in txt)

#Example with if
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")