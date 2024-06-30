# math/modulus.py
def mod(a, b):
    """
    Returns the modulus of a and b.
    """
    try:
        return a % b
    except TypeError:
        raise ValueError("Both arguments must be numbers.")