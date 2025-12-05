#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = list(map(lambda j: list(map(lambda x: x**2, j)), matrix))
    return square_matrix
