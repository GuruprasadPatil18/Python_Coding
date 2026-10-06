"""
Problem:
Write tests for validate() in numb3rs.py.

Approach:
I tested valid addresses like 1.2.3.4, 0.0.0.0 and 255.255.255.255. I also tested numbers above 255, addresses with too few or too many
parts, and inputs with letters like "cat" and "1.2.3.a".
"""
from numb3rs import validate

def test_valid_cases():
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_size():
    assert validate("275.3.6.28") == False
    assert validate("256.1.1.1") == False
    assert validate("1.1.1.256") == False

def test_length():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False

def test_diff_charc():
    assert validate("cat") == False
    assert validate("1.2.3.a") == False
