#!/usr/bin/python3
"""
This module demonstrates the use of Mixins in Python.
Mixins provide specific functionalities to a class through
multiple inheritance.
"""


class SwimMixin:
    """Mixin to provide swimming functionality."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to provide flying functionality."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Representing a Dragon that can swim and fly.
    This class combines behaviors from multiple Mixins.
    """

    def roar(self):
        """Prints a roaring message specific to the dragon."""
        print("The dragon roars!")
