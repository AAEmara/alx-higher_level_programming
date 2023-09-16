#!/usr/bin/python3

"""5-text_indentation module"""


def text_indentation(text):
    """Prints the text given with 2 new lines after '.', '?', and ':'
    characters.

    Raises:
        TypeError if text input isn't a string datatype.

    Args:
        text (string): String input to be formatted before printing the output.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if i == 0 and text[i] == " ":
            pass
        elif i == len(text) - 1 and text[i] == " ":
            pass
        elif text[i] == " " and (text[i + 1] == " " or text[i - 1] in " .?:"):
            pass
        elif text[i] in ['.', '?', ':']:
            print(f"{text[i]}\n")
        else:
            print(text[i], end="")
