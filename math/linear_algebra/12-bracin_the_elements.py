#!/usr/bin/env python3
""" bracin the elements
"""


import numpy as np


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1 (numpy.ndarray): The first matrix.
        mat2 (numpy.ndarray or scalar): The second matrix or scalar.

    Returns:
        tuple: A tuple containing the element-wise sum, difference, product,
          and quotient.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
