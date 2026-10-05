"""
Problem:
Write tests for convert() in working.py.

Approach:
Tested some valid inputs (with and without minutes, 12 AM and 12 PM, PM to AM shift) and some invalid ones (hour 13, minute 60, - instead of 'to', random text) to check that ValueError is raised.
"""

import pytest
from working import convert

def test_good_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_night_shift():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"

def test_bad_time():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")

def test_bad_format():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("cat")
