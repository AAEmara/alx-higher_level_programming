#!usr/bin/python3

"""2-append_write module."""


def append_write(file_name="", text=""):
    """Appends a string at the end of a text file using 'utf-8' encoding.

    Returns:
        Number of characters added.

    Args:
        file_name (string): path to the file or the filename.
        text (string): text to be appended at the end of the text file.
    """
    with open(file_name, mode='a', encoding='utf-8') as a_file:
        appended_bytes = a_file.write(text)

    return (appended_bytes)
