#!/usr/bin/python3
"""
This file provide an abstract Shape
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    This class provide two methods area and perimeter
    """
    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    This class provide two methods area and perimeter
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14159265359

    def perimeter(self):
        return 2 * self.radius * 3.14159265359


class Rectangle(Shape):
    """
    This class provide two methods area and perimeter
    """

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


def shape_info(obj):
    """
    Prints the area and perimeter of a shape using duck typing.
    Assumes the object has area() and perimeter() methods.
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
