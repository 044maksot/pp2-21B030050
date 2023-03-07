# 1. Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = '/Users/User/Documents/Programming/python/tsis6'
print("Only directories: ")
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("Only files: ")
print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("All directories and files: ")
print([name for name in os.listdir(path)])
print()

# 2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path.
import os
def check_path_access(path):
    access = {
        'Exists': os.path.exists(path),
        'Readable': os.access(path, os.R_OK),
        'Writable': os.access(path, os.W_OK),
        'Executable': os.access(path, os.X_OK)
    }
    return access
path = '/Users/User/Documents/Programming/python/tsis6'
access = check_path_access(path)
print(access)
print() 

# 3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
def testpath(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return f'Path exists. Filename: {filename}. Directory: {directory}'
    else:
        return 'Path does not exist'
path = '/Users/User/Documents/Programming/python/tsis6/example.txt'
result = testpath(path)
print(result)

# 4. Write a Python program to count the number of lines in a text file.
"""
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        count = len(lines)
    return count
filename = 'example.txt'
line_count = count_lines(filename)
print(f'The file "{filename}" has {line_count} lines.')
"""

# 5. Write a Python program to write a list to a file.
"""
def write_list_to_file(filename, lst):
    with open(filename, 'r') as file:
        for item in lst:
            file.write(f'{item}\n')
filename = 'example.txt'
my_list = ['apple', 'banana', 'orange', 'kiwi']
write_list_to_file(filename, my_list)
"""

# 6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string
def generate_files():
    for letter in string.ascii_uppercase:
        filename = f'{letter}.txt'
        with open(filename, 'w') as file:
            file.write(f'This is the file {filename}.\n')
generate_files()

# 7. Write a Python program to copy the contents of a file to another file.
"""
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
        contents = source.read()
        destination.write(contents)
source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)
"""

# 8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os
def delete_file(path):
    if not os.path.exists(path):
        print(f'Error: {path} does not exist.')
        return
    if not os.access(path, os.W_OK):
        print(f'Error: {path} is not writable.')
        return
    os.remove(path)
    print(f'{path} has been deleted.')
path = 'example.txt'
delete_file(path)