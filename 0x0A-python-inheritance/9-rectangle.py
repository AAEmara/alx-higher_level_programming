#!/usr/bin/python3

"""9-rectangle module"""

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
        self.__height = height

    def area(self):
        """Returns the are of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Printing or Returning a Rectangle class description."""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
