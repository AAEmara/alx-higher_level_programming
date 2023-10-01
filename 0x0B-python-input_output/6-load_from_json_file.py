#!/usr/bin/python3

"""6-load_from_json_file module"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (string): path to file or filename.
    """
    with open(filename, mode="r", encoding="utf-8") as r_file:
        file_str = r_file.read()

    return (json.loads(file_str))
