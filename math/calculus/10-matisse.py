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
    
    # Check if all elements in the list are integers or floats
    if not all(isinstance(coeff, (int, float)) for coeff in poly):
        return None
    
    # If the polynomial is constant (i.e., has only one term), return [0]
    if len(poly) == 1:
        return [0]
    
    # Compute the derivative: for each coefficient, multiply by its corresponding power of x
    derivative = [coeff * power for power, coeff in enumerate(poly) if power > 0]
    
    return derivative
