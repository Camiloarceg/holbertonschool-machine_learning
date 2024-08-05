#!/usr/bin/env python3
""" saddle up
"""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication on two numpy.ndarrays.

    Args:
        mat1 (numpy.ndarray): The first matrix.
        mat2 (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication.
    """
    return np.matmul(mat1, mat2)
