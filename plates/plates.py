"""
Problem:
Ask the user for a vanity plate and print "Valid" or "Invalid". The plate must start with 2 letters and be 2 to 6 characters long. 
Numbers can only come at the end and the first number cannot be 0. Spaces and punctuation are not allowed.

Approach:
I made an is_valid() function that returns True or False. First I check the length and that the first two characters are letters. 
Then I loop through the plate and when I find a digit, I check that everything after it is also a digit. I also check for 0 as the first number. 
At the end I use isalnum() to reject spaces and punctuation. In main() I take the input and print Valid or Invalid.
"""

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0" and i == 2:
                return False
            if not s[i:].isdigit():
                return False

    if not s.isalnum():
        return False

    return True


main()
