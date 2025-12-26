#!/usr/bin/python3
"""
function that returns the list of available attributes and methods of an object
python-inheritance.0-lookup
"""


def lookup(obj):
    """
    This function will return the list of methods an object

    :param obj: this is the object will return the list of methods
    """
    return dir(obj)
