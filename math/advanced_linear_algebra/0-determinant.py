#!/usr/bin/env python3
import numpy as np


def determinant(matrix):
    if not isinstance(matrix, list) and all(isinstance(el, list) for el in matrix):
        raise TypeError('matrix must be a list of lists')
    elif len(matrix) != len(matrix[0]):
        raise ValueError('matrix must be a square matrix')

    np_matrix = np.array(matrix)
    det = np.linalg.det(matrix)

    return det
