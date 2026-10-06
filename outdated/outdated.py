"""
Problem:
Ask the user for a date like "9/8/1636" or "September 8, 1636" and print it as YYYY-MM-DD. If the date is not valid, ask again.

Approach:
I made a list of month names and used a while loop with try/except. If the input has "/" in it, I split it into month, day and year. 
If not, I split it at the spaces and check that the month is in the list and the day ends with a comma. The month number is the index in the list plus 1. 
I check that the month is 1 to 12 and the day is 1 to 31, else I ask again. Then I print the date and break the loop.
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

            if month < 1 or month > 12 or day < 1 or day > 31:
                continue

        else:
            month, day, year = date.split(" ")

            if month not in months:
                continue

            if not day.endswith(","):
                continue

            day = int(day.replace(",", ""))

            if day < 1 or day > 31:
                continue

            month = months.index(month) + 1
            year = int(year)

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except ValueError:
        pass
