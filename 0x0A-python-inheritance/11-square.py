#!/usr/bin/python3

"""10-square module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):

    """Square class."""

    def __init__(self, size):
        """Instantiation of arguments for Square class.

        Raises:
            TypeError if the value of the argument is not an integer.
            ValueError if the value of the argument is less than or equal ZERO.

        Args:
            size (integer): represents the side lenght of a square.
        """
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """Prints or returns Square class description"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
