def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def square(a):
    return a ** 2

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Cannot take square root of a negative number!"
    return a ** 0.5
