#!/usr/bin/python3
"""Square class documentation"""


class Square(object):
    """A Square class that aims to create a square."""

    def __init__(self, size=0):
        """Initializing the class with the size of a square.

        Args:
            size (:obj:`int`, 0): represents the size of the square.

        """

        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Calculates the area of a square and returns it.

        Returns:
            Area of the square.
        """
        area = self.__size * self.__size
        return area
