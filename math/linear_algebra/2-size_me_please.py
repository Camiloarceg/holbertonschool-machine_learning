#!/usr/bin/env python3
""" size me please
"""


def matrix_shape(matrix):
    """ computes a matrix shape

    Args:
        matrix (matrix): the matrix to compute the shape of
    """

    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + matrix_shape(matrix[0])
