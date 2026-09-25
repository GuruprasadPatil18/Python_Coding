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
