#!/usr/bin/python3
"""Define a square class"""


class Square:
    """
    Represents a Square class used to calculate area and print a square
    with specific size and offset (position).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        :param size (int): The side length of the square. Default is 0.
        :param position (tuple): A tuple of 2 positive integers (x, y)
                                 for horizontal and vertical offset.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square.

        Validates that position is a tuple of 2 positive integers (x, y).
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square to stdout using the character '#'
        respecting the position (offset).
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        horizontal_offset = " " * self.__position[0]
        square_line = "#" * self.__size

        for i in range(self.__size):
            print(horizontal_offset + square_line)
