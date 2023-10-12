#!/usr/bin/python3
"""base module that includes the Base Class."""


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
