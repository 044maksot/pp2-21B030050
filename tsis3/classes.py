# 1. Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
class string:
    def init(self):
        self.s = ""

    def getstring(self):
        self.s = input()

    def printstring(self):
        print(self.s.upper())
s = string()
s.getstring()
s.printstring()

print()
# 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape:
    def area(self):
        print(0)
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        print(self.length ** 2)
sh = Shape()
sq = Square(2)
sh.area()
sq.area()

print()
# 3. Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class Rectange(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
rect = Rectange(2, 4)
rect.area()

# 4. Write the definition of a Point class. Objects from this class should have a
# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points


# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
# class Account:
    # pass
    
# 6. Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.