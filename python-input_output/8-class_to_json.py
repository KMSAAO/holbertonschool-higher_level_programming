#!/usr/bin/python3
"""
This file include class_to_json function
"""


def class_to_json(obj):
    """
    This function to return the dictionary description

    :param obj: This the object
    """

    return obj.__dict__
