x = 120
y = 180
if x > y:
    print("b is greater than a")
else:
    print("b is not greater than a")

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# will return false:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

def func():
    return True
if func():
    print("Yes")
else:
    print("No")