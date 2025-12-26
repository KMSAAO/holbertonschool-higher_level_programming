#!/usr/bin/python3
"""
This file include save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function to save the obj inside the file

    :param my_obj: the obj to save inside the file
    :param filename: the file to save the obj inside
    """

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))
