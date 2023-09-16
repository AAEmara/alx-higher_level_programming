#!/usr/bin/python3

"""4-inherits_from module"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited
    (directly/not directly) from a specified class.

     Args:
        obj (object): object to be checked against.
        a_class (class): specific class to check if the object inherited from.

    Returns:
        True if it inherited from the specified class (directly or not).
        False if it didn't inherit from the specified class (directly or not).

    """
    return isinstance(obj, a_class) and type(obj) != a_class
