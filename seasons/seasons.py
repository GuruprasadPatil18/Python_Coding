"""
Problem:
Ask the user for their date of birth in YYYY-MM-DD format and print
their age in minutes, written in words without "and". Example:
"Five hundred twenty-five thousand, six hundred minutes". If the date
is not in the right format, exit with an error message.

Approach:
I split the input at "-" to get the year, month and day, and made a
date from them. If it fails, I catch the ValueError and exit with
"Invalid date". I made a calculate_minutes() function that subtracts the
birth date from today's date to get the days and multiplies it by 24
and 60. Then I used the inflect package, which I installed with pip, to
change the number to words. I removed " and " from the words, made the
first letter capital and printed it with "minutes".
"""

from datetime import date
import sys
import inflect

def main():
    birth = input("Date of Birth: ")

    try:
        year, month, day = birth.split("-")
        birth_date = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()

    minutes = calculate_minutes(birth_date, today)

    p = inflect.engine()

    words = p.number_to_words(minutes)

    words = words.replace(" and ", " ")

    print(words.capitalize(), "minutes")


def calculate_minutes(birth_date, today):
    difference = today - birth_date

    minutes = difference.days * 24 * 60

    return minutes


if __name__ == "__main__":
    main()
