#!/usr/bin/python
"""
This file include read_file function
"""


def read_file(filename=""):
    """
    This function will read the file and prints it
    
    :param filename: The name of the file will read
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")