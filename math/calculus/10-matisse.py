#!/usr/bin/env python3
""" matisse
"""


def poly_derivative(poly):
    """ derivates a poly

    Args:
        poly (_type_): the plynomial

    Returns:
        _type_: the derivative of the polynomial
    """

    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not all(isinstance(coeff, (int, float)) for coeff in poly):
        return None

    if len(poly) == 1:
        return [0]

    derivative = [coeff * power for power,
                  coeff in enumerate(poly) if power > 0]

    return derivative
