#!/usr/bin/python3
"""Define a square class"""


class Square:
    """
    Represents a Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Insitializes a new Square

        :param size (int): its the size of the square, and the Default is 0
        :param position (tuple): should be set using space (-)
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """my_print will print in stdout the square with the charecter (#) """
        if self.__size == 0:
            print()
        else:
            y = 0
            for i in range(self.__size):
                while y < self.__position[1]:
                    print()
                    y += 1
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """
        Insitializes position

        :param value: is the value of __position
        """
        if not isinstance(value, tuple) and value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
