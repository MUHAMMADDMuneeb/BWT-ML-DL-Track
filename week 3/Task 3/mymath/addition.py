# math/addition.py
def add(a, b):
    """
    Returns the sum of a and b.
    """
    try:
        return a + b
    except TypeError:
        raise ValueError("Both arguments must be numbers.")