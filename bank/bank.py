"""
Problem:
Ask the user for a greeting. If it starts with "hello", print $0. If it starts with "h" but not "hello", print $20. Otherwise print $100.

Approach:
I took the input and used lower() and strip() so capital letters and spaces don't matter. Then I checked with startswith(). I check 'hello' first because it also starts with 'h'.
"""

greet = input("Greeting: ")
greet = greet.lower().strip()
if greet.startswith("hello"):
    print("$0")
elif greet.startswith("h"):
    print("$20")
else:
    print("$100")
