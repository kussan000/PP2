#1.Unpacking a Tuple

#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

#Example 1
fruits = ("apple", "banana", "cherry")

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

#Example 2
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#2.Using Asterisk*

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

#Example 1
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)  # apple
print(yellow) # banana
print(red)    # ["cherry", "strawberry", "raspberry"]

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

#Example 2
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)  # apple
print(tropic) # ["mango", "papaya", "pineapple"]
print(red)    # cherry

