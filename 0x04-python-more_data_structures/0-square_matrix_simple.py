#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(0, len(matrix)):
        new_matrix.append([])
        for col in range(0, len(matrix[row])):
            element = matrix[row][col]
            new_matrix[row].append(element * element)

    return new_matrix
