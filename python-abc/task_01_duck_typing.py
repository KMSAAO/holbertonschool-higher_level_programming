#!/usr/bin/python3
"""
This file provide an abstract Shape
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    This class provide two methods area and perimeter
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    This class provide two methods area and perimeter
    """

    def __init__(self, radius):
        if radius <= 0:
            return None
        self.rad = radius

    def area(self):
        return self.rad * self.rad * math.pi

    def perimeter(self):
        return 2 * self.rad * math.pi


class Rectangle(Shape):
    """
    This class provide two methods area and perimeter
    """

    def __init__(self, height, width):
        if height <= 0 or width <= 0:
            return None
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


def shape_info(obj):
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
