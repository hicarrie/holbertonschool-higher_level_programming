#!/usr/bin/python3
"""
Module to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix
    and return results in new matrix
    """

    """Checks for 0 division"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """Checks if div is a number"""
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    """Checks length of matrix rows"""
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    """Checks that matrix is made only of numbers"""
    for row in matrix:
        for i in range(len(row)):
            if not isinstance(row[i], int) and not isinstance(row[i], float):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    return [[round(row[i] / div, 2) for i in range(len(row))]
            for row in matrix]
