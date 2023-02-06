# If else
"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
""" 
a = 120
b = 180
if b > a: # if statement
    print("b is greater than a")
elif a == b: # elif statement
    print("a and b are equal")
else: # else statement
    print("a is greater than b")

# Short hand if
if a > b: print("a is greater than b")

# Short hand if else
a = 170
b = 150
print("a") if a > b else print("=") if a == b else print("b")

# And
a = 10
b = 5
c = 15
if a > b and c > a:
    print("Both conditions are true")

# Or
a = 15
b = 10
c = 20
if a > b or a > c:
    print("At least one of the conditions is true") 