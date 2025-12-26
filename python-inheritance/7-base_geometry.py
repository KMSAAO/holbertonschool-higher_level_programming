#!/usr/bin/python3
"""
this file will provides:
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
        else:
            return True
