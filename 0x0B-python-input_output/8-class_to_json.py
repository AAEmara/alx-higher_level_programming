#!/usr/bin/python3
"""8-class_to_json module."""


def class_to_json(obj):
    """Converts a python object into JSON serialization.

    Args:
        obj (any object type): object to be used for JSON serialization.
    """
    obj_dict = obj.__dict__
    return (obj_dict)
