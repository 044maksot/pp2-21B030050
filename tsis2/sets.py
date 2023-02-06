# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

"""
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
"""

# Duplicates not allowed because sets cannot have two items with the same value and will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Get the Length of a Set
# To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) 

# type()
# Sets are defined as objects with the data type 'set'
myset = {"apple", "banana", "cherry"}
print(type(myset))

# It is also possible to use the set() constructor to make a set
thisset = set(("apple", "banana", "cherry"))
print(thisset) # the set list is unordered, so the result will display the items in a random order.

