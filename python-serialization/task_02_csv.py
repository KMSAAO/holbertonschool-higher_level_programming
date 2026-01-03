#!/usr/bin/python3
"""
This file include convert_csv_to_json function
"""
import json
import csv


def convert_csv_to_json(filename):
    """
    This function converts CSV to JSON and handles exceptions.

    :param filename: The file to convert to json
    :return: True if successful, False if file not found
    """
    try:
        new_list = []

        with open(filename, "r", encoding="utf-8") as f:
            read = csv.DictReader(f)
            for row in read:
                new_list.append(row)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(new_list, f, indent=4)

        return True

    except FileNotFoundError:
        return False
