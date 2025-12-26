#!/usr/bin/python3
"""
This file include load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    This function will load from json file

    :param filename: the file to load file inside it
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
