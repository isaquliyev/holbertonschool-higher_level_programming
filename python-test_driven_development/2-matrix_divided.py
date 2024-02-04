#!/usr/bin/python3
"""
    The 1. Divide a matrix module.
    This module contain a function: matrix_divided
"""


def matrix_divided(matrix, div):
    """
        matrix_divided - This function divides all
        elements of a matrix.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    new_matrix = []
    row_length = len(matrix[0])
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        new_matrix.append([])
        if len(matrix[i]) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not (isinstance(matrix[i][j], int) or
                    isinstance(matrix[i][j], float)):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

            new_matrix[i].append(round(matrix[i][j] / div, 2))
    return new_matrix
