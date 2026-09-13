#!/usr/bin/env python3
"""Stuff"""


def matrix_shape(matrix):
    """
    docstring for matrix_shape
    dsfghnsdfghjgfd
    """
    shape = [len(matrix)]

    if isinstance(matrix[0], list):
        shape.extend(matrix_shape(matrix[0]))

    return shape


def add_matrices2D(mat1, mat2):
    """Stuff"""
    mat_final = [[0 for _ in range(len(mat1))]
                for _ in range(len(mat1[0]))]

    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    else:
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                mat_final[i][j] = mat1[i][j] + mat2[i][j]
        return mat_final
