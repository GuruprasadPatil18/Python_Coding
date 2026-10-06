"""
Problem:
Ask the user for some text and print how many times the word "um" appears in it. Capital letters should also count, and "um"
inside another word like "yummy" should not be counted.

Approach:
I made a count() function that uses re.findall with the pattern r"\bum\b". The \b makes sure "um" is a full word on its own,
so "yummy"is not counted. I used re.IGNORECASE so "UM" and "Um" are also found.
The function returns the number of matches. In main() I take the input and print the count.
"""

import re
import sys

def main():
    print(count(input("Input: ")))

def count(s):
    words = re.findall(r"\bum\b", s, re.IGNORECASE)

    return len(words)

if __name__ == "__main__":
    main()
