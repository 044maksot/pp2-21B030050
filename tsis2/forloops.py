# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
pc = ["monitor", "keyboard", "mouse"]
for a in pc:
    print(a)

# Looping through a string
for b in "kbtu":
    print(b)

# The break statement
pc = ["monitor", "keyboard", "mouse"]
for c in pc:
    print(c)
    if c == "keyboard":
        break

# The continue statement
pc = ["monitor", "keyboard", "mouse"]
for d in pc:
    if d == "keyboard":
        continue
    print(d)

# The range() function
for e in range(5, 10):
    print(e)

for x in range(2, 30, 3): # Increment the sequence with 3
    print(x)

for x in range(6):
    if x == 3: 
        break
    print(x)
else:
    print("Finally finished!") # If the loop breaks, the else block is not executed.

colors = ["red", "black", "green"]
fruits = ["apple", "banana", "cherry"]

for x in colors:
  for y in fruits:
    print(x, y)