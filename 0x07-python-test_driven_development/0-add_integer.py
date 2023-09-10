#!/usr/bin/python3

"""0-add_integer module"""


def add_integer(a, b=98):

    """Adds two integers or floats.

    Returns:
        Integer sum of given values.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
