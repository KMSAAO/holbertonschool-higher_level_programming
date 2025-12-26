#!/usr/bin/python3
"""
This file include append_write function
"""


def append_write(filename="", text=""):
    """
    This function will append in file

    :param filename: the file to append in
    :param text: the text to append in file
    """

    with open(filename, 'a', encoding="utf-8") as file:
        apText = file.write(text)
        return apText
