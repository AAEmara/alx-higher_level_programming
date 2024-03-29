#!/usr/bin/python3
"""rectangle module that constructs the Rectangle Class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class that create a Rectangle instance."""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates the area of a rectangle.

        Returns:
            Area of a rectangle.
        """
        area = self.__width * self.__height
        return (area)

    def display(self):
        """Displaying the Rectangle's instance shape using '#' character
        while taking into consideration the values of x and y.
        """
        print("\n" * self.__y, end="")
        for row in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Printing Rectangle's instance default string representation"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates the attributes of Rectangle's instance."""
        if len(args):
            attr = list(self.__dict__)
            for i, arg in enumerate(args):
                self.__dict__[attr[i]] = arg
        else:
            for key, val in kwargs.items():
                if key != "id":
                    setattr(Rectangle, key, val)
                else:
                    self.__dict__[key] = val

    def to_dictionary(self):
        """Returns a dictionary representation of the Rectangle Class."""
        keys = ["id", "width", "height", "x", "y"]
        new_dict = dict()
        for i, key in enumerate(self.__dict__):
            new_dict[keys[i]] = self.__dict__[key]

        return (new_dict)

    @property
    def width(self):
        """int: Integer value of the rectangle's width."""
        return (self.__width)

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """int: Integer value of the rectangle's height."""
        return (self.__height)

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """int: Integer value of the rectangle's x coordinate."""
        return (self.__x)

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """int: Integer value of the rectangle's y coordinate."""
        return (self.__y)

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
