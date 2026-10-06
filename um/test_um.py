"""
Problem:
Write tests for count() in um.py.

Approach:
I tested "um" once and twice, and "UM" in capital letters. I also
tested "yummy" and "gp" to check that they give 0. Then I tested "um"
with a question mark and a comma to check that punctuation does not
stop it from being counted.
"""
from um import count

def test_um():
    assert count("um") == 1

def test_multiple_um():
    assert count("um um") == 2

def test_uppercase():
    assert count("UM") == 1

def test_yummy():
    assert count("yummy") == 0

def test_gp():
    assert count("gp") == 0

def test_question():
    assert count("um?") == 1

def test_comma():
    assert count("um, hello") == 1
