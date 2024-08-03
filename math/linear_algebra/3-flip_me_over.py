#!/usr/bin/env python3

def matrix_transpose(matrix):
    """
    Transposes a 2D matrix by swapping rows and columns.

    Args:
        matrix (list): A 2D list representing the matrix.

    Returns:
        list: A new 2D list representing the transposed matrix.
    """
    # Create a new matrix with swapped dimensions
    transposed = [[None for _ in range(len(matrix))]
                  for _ in range(len(matrix[0]))]

    # Iterate over the original matrix and swap elements
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]

    return transposed
