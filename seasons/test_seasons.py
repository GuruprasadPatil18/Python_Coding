"""
Problem:
Write tests for calculate_minutes() in seasons.py.

Approach:
I tested one day (1440 minutes) and one full year (527040 minutes). I
also tested a date range with a leap day and the same date for both,
which should give 0.
"""

from datetime import date
from seasons import calculate_minutes

def test_one_day():
    birth_date = date(2020, 1, 1)
    today = date(2020, 1, 2)

    assert calculate_minutes(birth_date, today) == 1440

def test_one_year():
    birth_date = date(2020, 1, 1)
    today = date(2021, 1, 1)

    assert calculate_minutes(birth_date, today) == 527040

def test_leap_year():
    birth_date = date(2020, 2, 28)
    today = date(2020, 3, 1)

    assert calculate_minutes(birth_date, today) == 2880

def test_same_date():
    birth_date = date(2020, 1, 1)
    today = date(2020, 1, 1)

    assert calculate_minutes(birth_date, today) == 0
