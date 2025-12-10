#!/usr/bin/python3
"""Define a square class"""


class Square:
    """
    Represents a Square class
    """
    def __init__(self, size=0):
        """
        Insitializes a new Square

        :param size (int): its the size of the square, and the Default is 0
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Insitializes size

        :param value: is the value of __size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area is square any number"""
        square1 = self.__size * self.__size
        return square1
