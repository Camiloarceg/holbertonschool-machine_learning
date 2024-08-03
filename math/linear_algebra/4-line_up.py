#!/usr/bin/env python3

def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list): The first array.
        arr2 (list): The second array.

    Returns:
        list: A new array containing the sum of the corresponding elements from arr1 and arr2.
    """
    if len(arr1) != len(arr2):
        return None
    result = [arr1[i] + arr2[i] for i in range(len(arr1))]
    return result
