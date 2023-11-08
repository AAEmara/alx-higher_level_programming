#!/usr/bin/python3
"""base module that includes the Base Class."""
import json

class Base:
    """Base Class that manages the id attribute in all subclasses."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the instance of the Base class.

        Args:
            id (int): Unique identifier for each new instance created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returning JSON data representation of the list of dictionaries."""
        if list_dictionaries is None:
            return ("[]")
        else:
            json_obj = json.dumps(list_dictionaries)
            return (json_obj)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of a list of objects to a file."""

        filename = cls.__name__ + ".json"
        objs = list()
        with open(filename, mode="w", encoding="utf-8") as w_file:
            for obj in list_objs:
                objs.append(obj.to_dictionary())
            w_file.write(Base.to_json_string(objs))
