"""
Problem:
Take a text input from the user that has emoji codes like ":thumbs_up:" and print it with the codes changed to real emojis.

Approach:
I used the emoji package, which is installed with pip. I took the input and passed it to emoji.emojize() with language="alias" so that the shorter codes also work. Then I print the result.
"""

import emoji

text = input("Input: ")
print(emoji.emojize(text, language="alias"))
