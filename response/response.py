"""
Problem:
Ask the user for an email address and print "Valid" if it is a proper email, else print "Invalid".

Approach:
I used the validators package, which I installed with pip.
I took the email as input and checked it with validators.email().
If it returns True I print "Valid", else I print "Invalid".
"""

import validators

email = input("What's your email address? ")

if validators.email(email):
    print("Valid")
else:
    print("Invalid")
