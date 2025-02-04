#1.Python Numbers
"""
There are three numeric types in Python:
1.int
2.float
3.complex
"""

#Example 1
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Example Int
x = 1
y = 35656222554887711
z = -3255522

#Example Float
x = 1.10
y = 1.0
z = -35.59

#Float can also be scientific numbers with an "e" to indicate the power of 10.

#Example Float with 'e'
x = 35e3
y = 12E4
z = -87.7e100

#Example Complex
x = 3+5j
y = 5j
z = -5j

#2.Type Conversion

#Convert from int to float:
x = 4
a = float(x)

#Convert from float to int:
x = 2.3
b = int(x)

#Convert from int to complex:
x = -5
c = complex(x)

#3.Random Number

#First you should import random, than you need to ask range for random.

#Example 1
import random
a = random.randint(1, 10)
print(a)

