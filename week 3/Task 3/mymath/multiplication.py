# math/multiplication.py
def multiply(a, b):
    """
    Returns the product of a and b.
    """
    try:
        return a * b
    except TypeError:
        raise ValueError("Both arguments must be numbers.")