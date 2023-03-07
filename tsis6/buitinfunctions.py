# 1. Write a Python program with builtin function to multiply all the numbers in a list.
from functools import reduce
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)
numbers = [2, 3, 4, 5]
result = multiply_list(numbers)
print(result)
print()

# 2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters.
def count(string):
    upper = 0
    lower = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return (upper, lower)
string = input("")
result = count(string)
print("upper case: ", result[0])
print("lower case:", result[1])
print()

# 3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def palindrome(string):
    reversedstr = ''.join(reversed(string))
    return string == reversedstr
string = input("")
result = palindrome(string)
print(result)
print()

# 4. Write a Python program that invoke square root function after specific milliseconds.
import time
import math
def a(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)
number = float(input())
milliseconds = float(input())
result = a(number, milliseconds)
print(result)
print()

# 5. 
def alltrue(tup):
    return all(tup)
firsttup = (True, True, True)
secondtup = (True, False, True)
firstresult = alltrue(firsttup)
secondresult = alltrue(secondtup)
print(firstresult)
print(secondresult)
