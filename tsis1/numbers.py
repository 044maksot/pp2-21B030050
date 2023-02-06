"""
There are three numeric types in Python:
int
float
complex
"""

a = 23213 # int
b = -87.7e100 # float
c = 2 + 2j # complex
print(type(a), type(b), type(c))

# Type conversion
x = float(a)
y = int(b)
z = complex(a)
print(x, y, z)
print(type(x), type(y), type(z))