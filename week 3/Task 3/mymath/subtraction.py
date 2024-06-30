# math/subtraction.py
def subtract(a, b):
    """
    Returns the difference of a and b.
    """
    try:
        return a - b
    except TypeError:
        raise ValueError("Both arguments must be numbers.")