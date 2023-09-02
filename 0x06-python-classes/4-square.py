#!/usr/bin/python3
"""Square class documentation"""


class Square(object):
    """A Square class that aims to create a square."""

    def __init__(self, size=0):
        """Initializing the class with the size of a square.

        Args:
            size (:obj:`int`, 0): represents the size of the square.

        """
        self.__size = size

    def area(self):
        """Calculates the area of a square and returns it.

        Returns:
            Area of the square.
        """
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        """Getter function int: Returns the size value of the square.

        Setter function int: Changes the size of the square according to the
                             given value by the user.

            Args:
                value (int): value to be set as a square's size by the user.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Checks the type of the given argument against integer type,
        and also checks that the given value is not negative.

        if any of the checks succeeded it raises an exception to the user.

        else, it sets the given value by the user to the class attribute.

        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
