#!/usr/bin/python3


"""3-to_json_string module."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Returns:
        String object through using JSON representation.

    Args:
        my_obj (optional): Object to be represented as in JSON as a string.
    """
    str_obj = json.dumps(my_obj)

    return (str_obj)
