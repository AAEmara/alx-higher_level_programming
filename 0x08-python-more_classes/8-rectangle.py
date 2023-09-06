#!/usr/bin/python3
"""Rectangle class documentation"""


class Rectangle:
    """A Rectangle class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing the class with a rectangle.

        Args:
            height (int, 0): Height's initial value of the desired rectangle.
            width (int, 0): Width's initial value of the desired rectangle.
            print_symbol (int, "#"): Rectangle's symbol to be printed with.

        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

    @property
    def width(self):
        """Getter Function int: Returns the width of the rectangle.

        Setter Function int: Changes the width of the rectangle according to
                             the value given by the user.

            Args:
                width (int): Rectangle's width given by user.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Checks the width's value given by the user and raises an exception
        if an error occured.

            if the type of width argument is not an integer a TypeError
            exception is raised.

            else if the value of the width given is less than ZERO a ValueError
            exception is raised.

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter Function int: Returns the height of the rectangle.

        Setter Function int: Changes the height of the rectangle according to
                             the value given by the user.
            Args:
                height (int): Rectangle's height given by user.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Checks the height's value given by the user and raises an exception
        if an error occured.

            if the type of height argument is not an integer a TypeError
            exception is raised.

            else if the value of the height given is less than ZERO a
            ValueError exception is raised.

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle.

        If the width or height given is ZERO, the perimeter returned is ZERO.

        """
        if self.width == 0 or self.height == 0:
            return 0

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Returns the string to be printed to the user."""
        string = ""

        if self.width == 0 or self.height == 0:
            return string

        for i in range(self.height):
            for j in range(self.width):
                string += str(self.print_symbol)
            if i != (self.height - 1):
                string += "\n"

        return string

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Deletes an instance of the Rectangle class with a message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the areas of the given two rectangles.

        Note:
            Raises a TypeError if any of the arguments given by the user
            isn't a Rectangle class.

        Args:
            rect_1 (obj of Rectangle class): First instance of a Rectangle
                                             class.
            rect_2 (obj of Rectangle class): Second instance of a Rectangle
                                             class.

        Returns:
            rect_1 class instance if both areas are equal.
            rect_1 class instance if the area of rect_1 bigger than rect_2
            area.
            rect_2 class instance otherwise.

        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2
