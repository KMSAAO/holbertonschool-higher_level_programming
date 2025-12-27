#!/usr/bin/python3
"""
This file include serialize_and_save_to_file load_and_deserialize function
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    This to serialize the data and save it to file

    :param data: The data to serialize
    :param filename: The file to save data on it
    """
    with open(filename, "w", encoding="utf-8") as file:
        seri = file.write(json.dumps(data))

    return seri


def load_and_deserialize(filename):
    """
    This to load and deserialize data from the specidied file

    :param filename: The file to load from
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
