#!/usr/bin/python3
"""
This file include to_json_string function
"""
import json


def to_json_string(my_obj):
    """
    This fucntion to convert the obj to json string

    :param my_obj: the obj to convert to json string
    """
    return json.dumps(my_obj)
