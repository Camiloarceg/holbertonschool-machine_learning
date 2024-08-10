#!/usr/bin/env python3
""" sum total
"""


def summation_i_squared(n):
    """ summation of i squared
    """
    if not isinstance(n, int) or n < 1:
        return None

    return (n * (n + 1) * (2 * n + 1)) // 6
