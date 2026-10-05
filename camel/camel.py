"""
Problem:
Take a camelCase variable name from the user and print it in snake_case.
Example: "firstName" becomes "first_name".

Approach:
I looped through each character of the input. If the character is a capital letter, I add "_" and its lowercase form to a new string.
Otherwise I add the character as it is. Then I print the new string.
"""

cs = input("camelCase: ")

snake = ""

for i in cs:
    if i.isupper():
        snake += "_" + i.lower()
    else:
        snake += i

print("snake_case:",snake)
