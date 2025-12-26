#!/usr/bin/python3
"""
This file will provides a Public instance method area that raises
an Exception with the message area() is not implemented
"""


class BaseGeometry:
    """
    This class will provides a public instance method area
    """
    def area(self):
        raise Exception("area() is not implemented")
