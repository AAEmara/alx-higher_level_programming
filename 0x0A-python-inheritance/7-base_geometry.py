#!/usr/bin/python3

"""7-base_geometry module"""


class BaseGeometry:

    """BaseGeometry class."""
    def area(self):

        """Raises an exception because there is no implementation."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the type and the value of the `value` argument

        Raises:
            TypeError if the value argument is not an integer.
            ValueError if the value is less than or equal ZERO.

        Args:
            name (string): name of the integer value.
            value (integer): value of the integer variable.

        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
