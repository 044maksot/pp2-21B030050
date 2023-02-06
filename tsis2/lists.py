# Lists are used to store multiple items in a single variable.
mylist = ["apple", "banana", "cherry"]
print(mylist) 
print(len(mylist)) # to check the length of list
print(type(mylist)) # to check the type of list

# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # with the double round-brackets
print(thislist)