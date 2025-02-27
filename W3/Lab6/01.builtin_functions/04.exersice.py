import time
import math

def square(n, t):
    time.sleep(t / 1000)
    result = math.sqrt(n)
    
    return result

n = int(input("Enter your number: "))
t = int(input("Enter your time: "))

print("Square root of", n, "after", t, "miliseconds is", square(n, t))