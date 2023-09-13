#!/usr/bin/python3

"""Lookup Module"""


def lookup(obj):
    """Looks up the methods and attributes of an object

    Args:
        obj: The object to have its methods and attributes returned.

    Returns:
        list of methods and attributes
    """

    att_methods_list = list(dir(obj))
    return (att_methods_list)
