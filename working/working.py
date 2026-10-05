"""
Problem:
Convert working hours from 12 hour format to 24 hour format.
Example: "9:00 AM to 5:00 PM" becomes "09:00 to 17:00".
Minutes can be left out ("9 AM to 5 PM"). If the format or the time is wrong, raise ValueError.

Approach:
Used re.search to check the format and get hour, minute and AM/PM for both times. If it doesn't match, raise ValueError. Then each time goes
to convert_time(), which checks hour is 1-12 and minute is below 60.
12 AM becomes 0 and for PM I add 12 to the hour (except 12 PM).Finally both times are joined with 'to'.
"""

import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):

    matches = re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s)

    if not matches:
        raise ValueError

    hour1, minute1, ampm1, hour2, minute2, ampm2 = matches.groups()

    start = convert_time(hour1, minute1, ampm1)
    end = convert_time(hour2, minute2, ampm2)

    return start + " to " + end

def convert_time(hour, minute, ampm):
    hour = int(hour)

    if minute is None:
        minute = 0
    else:
        minute = int(minute)

    if hour < 1 or hour > 12:
        raise ValueError
    if minute > 59:
        raise ValueError

    if ampm == "AM" and hour == 12:
        hour = 0
    if ampm == "PM" and hour != 12:
        hour = hour + 12

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
