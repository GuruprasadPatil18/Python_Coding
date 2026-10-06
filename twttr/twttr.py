"""
Problem:
Take a text input from the user and print it without the vowels (a, e, i, o, u). Capital vowels should also be removed.

Approach:
I looped through the input one character at a time. If the character is not a vowel, I add it to a new string. I use lower() only for the
check, so the capital letters stay the same. Then I print the new string.
"""

wv = input("Input: ")

output = ""

for i in wv:
    if i.lower() not in "aeiou":
        output += i

print("Output:", output)
