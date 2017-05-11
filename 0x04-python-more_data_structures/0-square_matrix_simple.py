#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = lambda x: x * x
    new_matrix = [[list(map(square, row))] for row in matrix]
    return new_matrix
