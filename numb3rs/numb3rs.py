"""
Problem:
Ask the user for an IPv4 address and print True if it is valid, else print False.
A valid address has 4 numbers separated by dots, and each number is from 0 to 255.

Approach:
I made a validate() function that splits the address at ".". If there are not 4 parts, it returns False. Then I loop through
each part and check that it has only digits, that it does not start with 0 (unless it is just "0") and that it is not more than 255.
If any check fails it returns False, else it returns True. In main() I take the input and print the result.
"""
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:

        if not part.isdecimal():
            return False

        if len(part) > 1 and part[0] == "0":
            return False

        if int(part) > 255:
            return False

    return True

if __name__ == "__main__":
    main()
