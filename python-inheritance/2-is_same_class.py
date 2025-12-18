#!/usr/bin/python3
"""
 returns True if the object is exactly an instance of the specified class
    otherwise False.python-inheritance.2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an instance
    of the specified class ; otherwise False

    :param obj: the object want to check
    :param a_class: the format
    """
    return type(obj) is a_class
