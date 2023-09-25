#!/usr/bin/python3

"""1-write_file module."""


def write_file(file_name="", text=""):
    """Writes a string to a text file with 'utf-8' encoding.

    Returns:
        Number of characters written.

    Args:
        file_name (string): path to the file or filename.
        text (string): text to be written inside the filename given.
    """
    with open(file_name, mode='w', encoding='utf-8') as w_file:
        write_chars = w_file.write(text)

    return (write_chars)
