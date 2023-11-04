#!/usr/bin/python3
"""square module that constructs the Square Class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class which inherits from the Rectangle Class."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Updates the Square Class attributes."""
        attr = list(args)
        keys = list(self.__dict__)
        if len(args):
            for i, val in enumerate(args):
                if i == 2:
                    self.__dict__[keys[i]] = self.__dict__[keys[i - 1]]
                if i >= 2:
                    i += 1
                self.__dict__[keys[i]] = val
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    @property
    def size(self):
        """int: Integer value of the square's side length."""
        return (self.width)

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size
