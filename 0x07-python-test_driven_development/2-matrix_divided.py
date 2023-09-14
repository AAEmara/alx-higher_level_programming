#!/usr/bin/python3

"""``2-matrix_divided`` module"""


def matrix_divided(matrix, div):
    """Divides a matrix by a number (float or integer).

    Raises:
        TypeError if the matrix given is not a list type.
        TypeError if the rows of the matrix given aren't of a list type.
        TypeError if the rows lenghts aren't equal.
        TypeError if an element in the matrix isn't a float or an integer.
        TypeError if the divisor is not an integer or a float.
        ZeroDivisionError if the divisor is zero.

    Args:
        matrix (list of lists): a 2-D matrix of integers or floats.
        div (integer or float): the divisor of each element in the 2-D matrix.

    Returns:
        A new matrix where its elements are numbers and rounded to the nearst
        2 digits.
    """

    max_len = 0
    i = 0
    if isinstance(matrix, list):
        new_matrix = []
    else:
        raise TypeError("matrix must be a matrix (list of lists) of" +
                        " integers/floats")

    for row in matrix:
        if not (isinstance(row, list)):
            raise TypeError("matrix must be a matrix (list of lists) of" +
                            " integers/floats")
        if max_len < len(row):
            max_len = len(row)

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if max_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        new_matrix.append([])

        for col in row:
            if isinstance(col, int) or isinstance(col, float):
                new_matrix[i].append(round(col / div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
        i += 1

    return (new_matrix)
