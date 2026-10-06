"""
Problem:
Take a text input from the user and print it without the vowels (a, e, i, o, u). Capital vowels should also be removed.

Approach:
I made a shorten() function that goes through the text one character at a time. If the character is not a vowel, I add it to a new string. I
use lower() only for the check, so capital letters stay as they are. The function returns the new string. In main() I take the input and print the result.
"""

def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    output = ""

    for i in word:
        if i.lower() not in "aeiou":
            output += i

    return output


if __name__ == "__main__":
    main()
