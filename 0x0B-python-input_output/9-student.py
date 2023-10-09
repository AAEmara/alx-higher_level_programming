#!/usr/bin/python3
"""9-student module."""


class Student:
    """Student class.

    Args:
        first_name (str): Student's first name.
        last_name (str): Student's last name.
        age (int): Student's age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts python's class instance into a json form

        Returns:
            Dictionary data structure including all the instance attributes.
        """
        return (self.__dict__)
