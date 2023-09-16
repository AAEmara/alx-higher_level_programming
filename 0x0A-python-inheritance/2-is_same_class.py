#!/usr/bin/python3

"""2-is_same_class module."""


def is_same_class(obj, a_class):

    """Checks if an object is an exact instance of the specified class.

    Args:
        obj (object): object type to be checked.
        a_class (class): class to check the object against.

    Returns:
        True if the object is an exact instance of the specified class.
        False if the object is not an exact instance of the specified class.

    """
    if not (type(obj) == a_class):
        return False
    else:
        return True
