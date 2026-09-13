#!/usr/bin/env python3
"""Do stuff"""


def matrix_shape(matrix):
    """
    docstring for matrix_shape
    dsfghnsdfghjgfd
    """
    shape = [len(matrix)]

    if isinstance(matrix[0], list):
        shape.extend(matrix_shape(matrix[0]))

    return shape
