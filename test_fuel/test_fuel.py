"""
Problem:
Write tests for convert() and gauge() in fuel.py.

Approach:
I tested convert() with 1/2, 1/4 and 3/4 to check the percentage. I also checked that ValueError is raised for 5/4, -1/2, cat/dog and 1/-2,
and ZeroDivisionError for 1/0. For gauge() I tested 0 and 1 for E, 99 and 100 for F, and 50 for a normal percentage.
"""

from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75

def test_convert_invalid_cases():
    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ValueError):
        convert("-1/2")

    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("1/-2")

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge_EF():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
