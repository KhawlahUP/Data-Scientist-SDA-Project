from calculator import subtract

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3
    assert subtract(3, 3) == 0
