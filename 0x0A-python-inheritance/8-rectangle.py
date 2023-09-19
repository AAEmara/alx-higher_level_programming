#!/usr/bin/python3

"""8-base_geometry module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    """Rectangle class."""

    def __init__(self, width, height):
        """Instantiation of arguments for Rectangle class.

        Raises:
            TypeError if the value of one or more of the arguments is not an
            integer.
            ValueError if the value of one or more of the arguments is less
            than or equal ZERO.

        Args:
            width (integer): width of the rectangle.
            height (integer): height of the rectangle.

        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__heigth = height
