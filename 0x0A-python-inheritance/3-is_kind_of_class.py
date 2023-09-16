#!/usr/bin/python3

"""3-is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """Checks if the object given is an instance of a superclass or subclass.

    Args:
        obj (object): object given to be checked against super/subclass.
        a_class (class): class to have the object checked against.

    Returns:
        True if the object is an instance of a superclass or a subclass.
        False if the object is neither an instance of a superclass or sublass.

    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
