"""
Problem:
Ask the user for a fraction like "1/4" and print it as a percentage.If the percentage is 1 or less, print E. If it is 99 or more, print F.
If the input is not valid, ask again.

Approach:
I used a while loop with try/except so it keeps asking till the input is valid. I split the input at "/" and changed both parts to int. 
If x is negative or bigger than y, I ask again. Then I find the percentage and round it. 
If the input is in the wrong format or y is 0, the errors are caught and it asks again. After printing, I break the loop.
"""

while True:
    try:
        x, y = input("Fraction: ").split("/")

        x = int(x)
        y = int(y)

        if x < 0 or x > y:
            continue

        percentage = round((x / y) * 100)

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")

        break

    except ValueError:
        pass

    except ZeroDivisionError:
        pass
