#!/usr/bin/python3
"""rectangle module that constructs the Rectangle Class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class that create a Rectangle instance."""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """int: Integer value of the rectangle's width."""
        return (self.__width)

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """int: Integer value of the rectangle's height."""
        return (self.__height)

    @height.setter
    def height(self, height):
        self.__height = height
