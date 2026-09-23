from c3 import hello

def test_default():
    assert hello() == "hello, guruprasad"

def test_argument():
    assert hello("gp") == "hello, gp"
