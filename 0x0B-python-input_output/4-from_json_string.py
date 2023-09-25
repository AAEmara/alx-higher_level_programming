#!/usr/bin/python3


"""4-from_json_string module."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Returns:
        Object through using JSON string representation.

    Args:
        my_obj (string): Object represented by a JSON string.
    """
    str_obj = json.loads(my_str)

    return (str_obj)
