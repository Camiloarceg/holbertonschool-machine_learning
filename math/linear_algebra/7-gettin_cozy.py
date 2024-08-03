#!/usr/bin/env python3

""" getting cozy
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ Concatenates two matrices along a specified axis
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
