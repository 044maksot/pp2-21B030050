"""
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""
x = 5
y = 5
print(x + y) # addition
print(x - y) # subtraction
print(x * y) # multiplication
print(x / y) # division
print(x % y) # modulus
print(x ** y) # exponentiation
print(x // y) # floor division

a = 5 
a += 5 # is the same as a = a + 5 (increasing a by one)	
a -= 5 # is the same as a = a - 5 (decreasing a by one)
a *= 5 # is the same as a = a * 5 (multipliying a by 5 and assigning it to a)
a /= 5 # is the same as a = a / 5 (dividing a by 5 and assigning the value to a)
a %= 5 # is the same as a = a % 5 (modulus a by 5 and assigning it to a)
a //= 5	# is the same as a = a // 5	(floor dividing by 5 and assigning back)
a **= 5	# is the same as a = a ** 5	(finding power 5 and assigning it to a)
a &= 5 # is the same as a = a & 5 (assigning result of a AND 5 to a)
a |= 5 # is the same as a = a | 5 (assigning result of a OR 5 to a)
a ^= 5 # is the same as a = a ^ 5 (assigning result of a XOR 5 to a)
a >>= 5	# is the same as a = a >> 5 (shifting bits of a to 5 left and assigning back to a)
a <<= 5	# is the same as a = a << 5 (shifting bits of a to 5 right and assigning back to a)

# Comparison operators
a = 1
b = 2
print(a == b) # is x eqauls b
print(a != b) # is x not equals to b
print(a > b) # is x greater than b
print(a < b) # is x less than b
print(a >= b) # is x greater or equals to b
print(a <= b) # is x less or equals to b