#!/usr/bin/python3
"""
This module provides a function checks if an object is
an instance of class that inherited (directly or indirectly)
in a specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited from a_class.

    Args:
        obj: The object to check
        a_class: The class to match againts

    Return:
        True if obj inherits from a_class, otherwise False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
