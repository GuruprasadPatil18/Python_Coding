"""
Problem:
Take a Python file name as a command-line argument and print how many lines of code it has. Blank lines and comment lines (starting with #)
are not counted. If the number of arguments is wrong, the file is not a .py file, or the file does not exist, exit with an error message.

Approach:
I used sys.argv to check that there is exactly one argument and that it ends with ".py". I opened the file with try/except to handle
FileNotFoundError. Then I looped through the lines and skipped the ones that are empty or start with "#". For every other line I add 1 to the
count. At the end I close the file and print the count.
"""


import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

count = 0

for line in file:
    if line.strip() == "":
        continue
    if line.lstrip().startswith("#"):
        continue
    count = count + 1

file.close()
print(count)
