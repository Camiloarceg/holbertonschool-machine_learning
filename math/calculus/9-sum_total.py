#!/usr/bin/env python3
""" sum total
"""

def summation_i_squared(n):
    """ Sumatory of x squared
    Args:
        n (int): number of iterations
    Returns:
        int: sumatory of x squared
    """
    if not isinstance(n, int) or n < 1:
        return None

    if n == 1:
        return 1

    return n**3 + summation_i_squared(n - 1)
