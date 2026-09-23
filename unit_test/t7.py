from c3 import hello

def test_hello():
    assert hello("Gp") == "hello, Gp"
    assert hello() == "hello, guruprasad"
