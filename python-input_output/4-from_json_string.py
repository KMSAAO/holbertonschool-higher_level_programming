#!/usr/bin/python3
"""
This file include from_json_string function
"""
import json


def from_json_string(my_str):
    """
    This function to convert from json string to obj

    :param my_str: the str to convert
    """
    return json.loads(my_str)
