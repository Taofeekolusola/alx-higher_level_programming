#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[a ** 2 for a in x] for x in matrix]
    return new_matrix
