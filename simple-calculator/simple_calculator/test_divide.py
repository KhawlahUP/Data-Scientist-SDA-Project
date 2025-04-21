from calculator import divide

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(5, 0) == "Cannot divide by zero!"
