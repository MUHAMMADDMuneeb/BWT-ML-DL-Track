# math/sqrt.py
def sqrt(a):
    """
    Returns the square root of a.
    """
    try:
        if a < 0:
            raise ValueError("The input must not be negative.")
        return a ** 0.5
    except TypeError:
        raise ValueError("The argument must be a number.")
