from twttr import shorten


def test_lowercase():
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_mixed_case():
    assert shorten("Hello World") == "Hll Wrld"

def test_numbers():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"
