from calculator import sqrt

def test_sqrt():
    assert sqrt(9) == 3
    assert sqrt(0) == 0
    assert sqrt(-1) == "Cannot take square root of a negative number!"
