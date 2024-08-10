#!/usr/bin/env python3
""" integrate
"""


def poly_integral(poly, C=0):
    """ calculates ply integrals
    """
    if not isinstance(poly, list) or not all(isinstance(coeff, int)
                                             for coeff in poly):
        return None
    if not isinstance(C, int):
        return None
    if len(poly) == 1 and poly[0] != 0:
        return [C]

    integral_poly = [C]

    for power, coeff in enumerate(poly):
        new_coeff = coeff / (power + 1)
        integral_poly.append(int(new_coeff) if new_coeff.is_integer()
                             else new_coeff)

    while len(integral_poly) > 1 and integral_poly[-1] == 0:
        integral_poly.pop()

    return integral_poly
