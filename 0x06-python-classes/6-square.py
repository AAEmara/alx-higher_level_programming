#!/usr/bin/python3
"""Square class documentation"""


class Square(object):
    """A Square class that aims to create a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the class with the size of a square.

        Args:
            size (:obj:`int`, 0): represents the size of the square.
            position (:obj:`tuple` of :obj:`int`, (0,0)): represents the
                                                    position in a square.

        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of a square and returns it.

        Returns:
            Area of the square.

        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Prints a square according to the size given using '#' character,
        and the position given with space character.

        Note:
            If the size given is equal to ZERO a newline will be printed.
            If position[1] is bigger than ZERO a newline will be printed
            by the number of times given in position[1].

        """

        if self.__size == 0:
            print()
            return

        for line in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """Getter function int: Returns the size value of the square.

        Setter function: Changes the size of the square according to the
        given value by the user.

            Args:
                value (int): value to be set as a square's size by the user.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Checks the type of the given argument against integer type,
        and also checks that the given value is not negative.

        Note:
            if any of the checks succeeded it raises an exception to the user.

            else, it sets the given value by the user to the class attribute.

        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Getter function :obj:`tuple` of :obj:`int`: Returns the position
                                            inside a square.

        Setter function: Sets the position inside the square as given by user.

            Args:
                value :obj:`tuple` of :obj:`int`: A tuple that contains two
                integer values that represents the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Checks the type of the value and the number of items inside it
        before setting the position inside the square.

            Note:
                if the type of the value given isn't a tuple
                OR
                if the number of the items inside the tuple isn't 2,
                an exception is raised.

        """
        if (type(value) is not tuple) or (len(value) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')

        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')

        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value
