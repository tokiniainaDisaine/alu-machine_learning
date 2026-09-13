#!/usr/bin/env python3
"""Do stuff"""

def matrix_transpose(matrix):
    """Does stuff"""
    matrix_t = []

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix_t[j][i] = matrix[i][j]

    return matrix_t