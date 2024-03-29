#!/usr/bin/python3
"""Square class documentation"""


class Square(object):
    """A Square class that aims to create a square."""

    def __init__(self, size=None):
        """Initializing the class with the size of a square.

        Args:
            size (optional): represents the size of the sqaure.

        """
        self.__size = size
