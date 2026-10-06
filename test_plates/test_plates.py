"""
Problem:
Write tests for is_valid() in plates.py.

Approach:
I tested a valid plate (GP18). Then I tested plates that are too short or too long, plates that don't start with two letters, a number that
starts with 0, a letter after the number, and plates with a hyphen or a space.
"""

from plates import is_valid

def test_valid():
    assert is_valid("GP18") == True

def test_length():
    assert is_valid("G") == False
    assert is_valid("GP1234567") == False

def test_startwith():
    assert is_valid("1P") == False
    assert is_valid("G1") == False

def test_numbers_ending():
    assert is_valid("GP08") == False
    assert is_valid("GP18A") == False

def test_spacing_hypen():
    assert is_valid("GP-18") == False
    assert is_valid("GP 18") == False
