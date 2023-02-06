# 1. A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces.
grams = 10
ounces = 28.3495231 * grams
print(ounces)

# 2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion.
# C = (5 / 9) * (F – 32)
#def fahrenheit():
#    return (5 / 9) * (f - 32)
"""
f = 86
c = fahrenheit()
print("{0} centigrade".format(c))
"""
f = 86
c = (5 / 9) * (f - 32)
print("{0} centigrade".format(c))
 
# 3. Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
numheads = 35
numlegs = 94
def solve(nh, nl):
      if(nl > nh): # and (legs % 2 == 0):
        rabbit = (nl - 2 * nh) // 2
        chick = nh - rabbit
        print(f'There are {rabbit} Rabbits and {chick} chickens.')  
solve(numheads, numlegs) 

# 4. You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
'''def filter_prime(nums):
    primes = []
    isPrime = True
    for num in nums:
        for div in range(2, int(sqrt(num))):
            if num % div == 0:
                isPrime = False
                break
        if isPrime is True:
            primes.append(num)
        isPrime = True
    return primes
nums = list(map(int, input().split()))
print(filter_prime(nums))
'''

# 5. Write a function that accepts string from user and print all permutations of that string.

# 6. Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

# 7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
'''
def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False 
'''

# 8. Write a function that takes in a list of integers and returns True if it contains 007 in order
'''
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
'''

# 9. Write a function that computes the volume of a sphere given its radius.
pi = 3.142
radius = 6
r = radius ** 3
v = (4 / 3) * pi * r
print(v)

# 10. Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def unique(a):
    numbers = []
    for b in a:
        if b not in numbers:
            numbers.append(b)
    return numbers
print(unique([2, 3, 5, 5, 8, 11, 11, 11, 11, 45, 32, 2])) 

# 11. Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
string = input()
reverse = ""
for i in string:
    reverse = i + reverse
if(string == reverse):
    print("palindrome") 
else:
    print("not palindrome")   

# 12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# ******
def histogram(a):
    for n in a:
        out = ""
        times = n
        while(times > 0):
            out += '*'
            times = times - 1
        print(out)
histogram([4, 9, 7])

# 13. Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
'''
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
'''

import random
name = input("Hello! What is your name?")
print("Well, KBTU, I am thinking of a number between 1 and 20.")
guessed_num = random.randint(1, 20)
guess = 0
num_guesses = 0
while guess != guessed_num:
    print("Take a guess")
    guess = int(input())
    num_guesses += 1
    if guess < guessed_num:
        print('Your guess is too low.')
    elif guess > guessed_num:
        print('Your guess is too high')
    else:
        print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
        break

# 14. Create a python file and import some of the functions from the above 13 tasks and try to use them.