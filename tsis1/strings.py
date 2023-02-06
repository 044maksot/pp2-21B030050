print("hi")
# is the same as
print('hi')

a = 'hi'
print(a)

a = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(a)

a = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(a)

# String arrays
a = "How are you?" 
print(a[4]) # print will be 'a'

for a in "kbtu":
    print(a)

a = "hello, kbtu"
print(len(a))

txt = "The best things in life are free!"
if "best" in txt:
  print("There is")
else:
    print("There is no")