from mpmath import zetazero

def f(n):
    """
    Calculate the imaginary part of the n-th nontrivial zero of the Riemann zeta function.

    Args:
    - n (int): The integer argument for the Riemann zeta function.

    Returns:
    - float: The imaginary part of the n-th nontrivial zero of the Riemann zeta function.

    Note:
    The function returns 0.0 if n is less than or equal to 0.
    """
    return 0. if n <= 0 else float(zetazero(n).imag)



def find(f, y, a, b):
    """"
    Find an integer n in the range [a, b] such that f(n) equals y using binary search.

    Args:
    - f: A function that takes an integer argument and returns a floating-point value.
    - y: The target floating-point value.
    - a: The lower bound of the range (inclusive).
    - b: The upper bound of the range (inclusive).

    Returns:
    - If there exists an integer n in the range [a, b] such that f(n) equals y, return n.
    - If no such n is found, return -1.
    """
    while a <= b:
        mid = (a + b) // 2
        mid_value = f(mid)

        if mid_value == y:
            return mid
        elif mid_value < y:
            a = mid + 1
        else:
            b = mid - 1

    return -1

