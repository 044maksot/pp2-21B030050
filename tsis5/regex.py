import re
# 1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
pat1 = re.compile(r"ab*")
# 2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
pat2 = re.compile(r"ab{2,3}")
# 3. Write a Python program to find sequences of lowercase letters joined with a underscore.
pat3 = re.compile(r"[a-z]+\_")
# 4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
pat4 = re.compile(r"[A-Z]{1}[a-z]+")
# 5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
pat5 = re.compile(r"a.+b\Z")
# 6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
pat6 = re.compile(r"[ ,.]")
# 7. Write a python program to convert snake case string to camel case string.
import re
def camel(word):
    user = input("")
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
print(camel(user))
# 8. Write a Python program to split a string at uppercase letters.
import re
text = input("")
print(re.findall('[A-Z][^A-Z]*', text))
print()
# 9. Write a Python program to insert spaces between words starting with capital letters.
import re
def words(str1):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
user = input("")
print(words(user))
print()
# 10. Write a Python program to convert a given camel case string to snake case.
import re
def snake(text):
    user = input("")
    string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower()
print(snake(user))