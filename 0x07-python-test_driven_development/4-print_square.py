#!/usr/bin/python3

"""4-print_square module"""


def print_square(size):
    """Prints a square with a given size.

    Raises:
        TypeError if size is float and less than ZERO
        TypeError if size is not an integer value
        ValueError if size is less than ZERO

    Args:
        size (integer): represents the number of '#' character in a square.

    """
    if (isinstance(size, float) and (size < 0)) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
