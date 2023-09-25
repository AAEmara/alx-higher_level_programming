#!/usr/bin/python3

"""5-save_to_json_file module."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON representation.

    Args:
        my_obj (optional): Object to be written in a filename.
        filename (string): path to the file or filename.
    """
    with open(filename, mode='w', encoding='utf-8') as w_file:
        json.dump(my_obj, w_file)
