#!/usr/bin/python3

"""3-say_my_name module"""


def say_my_name(first_name, last_name=""):

    """Prints the first and last name of a person.

    Raises:
        TypeError if the first_name is not a string.
        TypeError if the last_name is not a string.

    Args:
        first_name (string): First name of the given person.
        last_name (string): Last name of the given person.

    Returns:
        Nothing.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
