#!/usr/bin/python3

"""0-read_file module."""


def read_file(file_name=""):
    """Reads a text file with UTF-8 encoding and prints to STDOUT.

    Args:
        file_name (string): the relative path to the file or the filename.
 
    """
    with open(file_name, mode='r', encoding='utf-8') as r_file:
        print(r_file.read())
