"""
Problem:
Ask the user for the cost of a meal and the tip percentage, then print the tip to leave. The meal cost can have a $ sign (like "$50.00") and
the percentage can have a % sign (like "15%"). The tip is printed with a $ sign and 2 decimal places.

Approach:
I made a dollars_to_float() function that removes the "$" and changes the text to a float. I made a percent_to_float() function that removes
the "%", changes it to a float and divides by 100. In main() I take both inputs, send them to these functions and multiply the meal cost by the
percent to get the tip. Then I print it.
"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$","")
    d=float(d)
    return d

def percent_to_float(p):
    p = p.replace("%","")
    p=float(p)
    return p/100

main()
