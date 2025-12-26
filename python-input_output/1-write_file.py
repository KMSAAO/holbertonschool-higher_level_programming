#!/usr/bin/python3
"""
This file include write_file function
"""


def write_file(filename="", text=""):
    """
    This function will write text inside a file

    :param filename: the file to write the text in
    :param text: the text to write in the file
    """

    with open(filename, 'w', encoding="utf-8") as file:
        textfile = file.write(text)
        return textfile
