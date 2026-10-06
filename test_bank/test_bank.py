"""
Problem:
Write tests for the value() function in bank.py.

Approach:
I tested "hello" for 0, "hi" for 20 and "good morning" for 100. I also tested "HELLO" to check that capital letters don't change the result.
"""

from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("hi") == 20

def test_other():
    assert value("good morning") == 100

def test_case():
    assert value("HELLO") == 0
