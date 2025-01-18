# Instructions:
# Create a custom Python module named calculator.py that contains functions for basic arithmetic operations (addition, subtraction, multiplication, division).
# Create functions add, subtract, multiply, and divide in the calculator.py module.
# Import the calculator module into a separate Python script main.py and use its functions to perform arithmetic operations on numbers like 5 and 3.

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the division of a by b."""
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"
