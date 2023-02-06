"""
Python has two primitive loop commands:

while loops
for loops
"""
i = 5
while i <= 10:
    print(i)
    i = i + 1
print()

# Break statement
i = 5
while i < 15:
    print(i)
    if i == 10:
        break
    i = i + 1
print()

# Continue statement
i = 3
while i < 10:
    i = i + 1
    if i == 5:
        continue
    print(i)