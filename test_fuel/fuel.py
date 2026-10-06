"""
Problem:
Ask the user for a fraction like "1/4" and print it as a percentage. If the percentage is 1 or less, print E. If it is 99 or more, print F.
If the input is not valid, print nothing.

Approach:
I made a convert() function that splits the fraction at "/" and change both parts to int. If y is 0 it raises ZeroDivisionError.
If x is negative or bigger than y it raises ValueError. Otherwise it returns the rounded percentage. The gauge() function returns E, F or the
percentage with a % sign. In main() I use try/except and do nothing if the input is wrong.
"""

def main():
    fraction = input("Fraction: ")

    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError):
        pass


def convert(fraction):
    x, y = fraction.split("/")

    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError

    if x < 0 or x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
