#!/usr/bin/python3
"""
This file wil provides a class rectangle that inherits from BaseGeometry
Public instance method (area) that raises an Exception with a message
Public instance method (integer_validator)that validates value
"""


class BaseGeometry:
    """
    This class will provides a public instance method area
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(self.value) is not int:
            raise TypeError(f"{self.name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This class provides an Instantiation with width and height
    """
    def __init__(self, width, height):
        bg = BaseGeometry()
        self.__width = width
        self.__height = height
        bg.integer_validator("width", self.__width)
        bg.integer_validator("height", self.__height)
