# math/division.py
def divide(a, b):
    """
    Returns the quotient of a divided by b.
    """
    try:
        if b == 0:
            raise ValueError("The divisor (b) must not be zero.")
        return a / b
    except TypeError:
        raise ValueError("Both arguments must be numbers.")