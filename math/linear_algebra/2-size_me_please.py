#!/usr/bin/env python3

def matrix_shape(matrix):
    shape = []

    while True:
        if type(matrix[0]) == "list":
            matrix_shape(matrix[0])
        elif type(matrix[0]) == "int":
            shape.insert(0, len(matrix))
            break
        else:
            shape.insert(0, len(matrix))

    return shape
