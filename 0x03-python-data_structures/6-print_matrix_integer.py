#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        pass
    else:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if j == len(matrix[i]) - 1:
                    print(matrix[i][j], end="")
                else:
                    print(matrix[i][j], end=" ")

            print()
