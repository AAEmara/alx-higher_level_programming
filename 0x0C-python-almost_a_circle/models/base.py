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
            if list_objs is None:
                w_file.write("[]")
            else:
                for obj in list_objs:
                    objs.append(obj.to_dictionary())
                w_file.write(Base.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list JSON string representation from a JSON string."""
        if json_string is None:
            json_repr = json.loads("[]")
        else:
            json_repr = json.loads(json_string)
        return (json_repr)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set."""
        if cls.__name__ == "Rectangle":
            instance = cls(width=5, height=5, x=0, y=0)
        elif cls.__name__ == "Square":
            instance = cls(size=5, x=0, y=0)
        instance.update(**dictionary)
        return (instance)
