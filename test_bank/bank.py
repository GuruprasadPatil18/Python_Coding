"""
Problem:
Ask the user for a greeting. If it starts with "hello", print $0. If it starts with "h" but not "hello", print $20. Otherwise print $100.

Approach:
I made a value() function that changes the greeting to lowercase and checks it with startswith(). It returns 0 for "hello", 20 for other
words starting with "h" and 100 for everything else. I check "hello" first because it also starts with "h". In main() I take the input and
print the value with a $ sign.
"""

def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 0

    elif greeting.startswith("h"):
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
