#!/usr/bin/python3
"""
this file will provide square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this class will calculate the area of the square
    """

    def __init__(self, size):
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        result = f"[Square] {self.__size}/{self.__size}"
        return result
