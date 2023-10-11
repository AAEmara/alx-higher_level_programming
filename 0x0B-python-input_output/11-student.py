#!/usr/bin/python3
"""11-student module."""


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

    def to_json(self, attrs=None):
        """Converts python's class instance into a json form.

        Description:
            If the attrs variable is a list object then it returns the selected
            items in the list as a dictionary data strucutre.
            Else it returns all the items as a dictionary data structure.

        Returns:
            Dictionary data structure including all the instance attributes.
        """
        json_obj = dict()

        if isinstance(attrs, list):
            for key in attrs:
                try:
                    json_obj[key] = self.__dict__[key]
                except KeyError:
                    pass
            return (json_obj)

        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """Replacing all the attributes of Student instance from json
        representation.

        Args:
            json (dictionary): JSON obj which is represented as a python dict.
        """
        return (json)
