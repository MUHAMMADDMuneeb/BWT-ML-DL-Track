# math/exponentiation.py
def power(a, b):
    """
    Returns a raised to the power of b.
    """
    try:
        return a ** b
    except TypeError:
        raise ValueError("Both arguments must be numbers.")
