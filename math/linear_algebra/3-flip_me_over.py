#!/usr/bin/env python3
"""Do stuff"""


def matrix_transpose(matrix):
    """Does stuff"""
    matrix_t = [[0 for _ in range(len(matrix))]
                for _ in range(len(matrix[0]))]

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix_t[j][i] = matrix[i][j]

    return matrix_t
