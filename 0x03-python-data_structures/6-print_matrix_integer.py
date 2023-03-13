#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for row in matrix:
            for col_i in range(len(row)):
                if col_i <= (len(row) - 2):
                    print("{:d}".format(row[col_i]), end=" ")
                else:
                    print("{:d}".format(row[col_i]))
