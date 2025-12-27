#!/usr/bin/python3
"""
This file include serialize_to_xml deserialize_from_xml function
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    This function convert dict to xml format
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)

        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")
    return True


def deserialize_from_xml(filename):
    """
    This function read the file and convert the content to dict
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result_dict = {}

        for child in root:
            result_dict[child.tag] = child.text
        return result_dict

    except FileNotFoundError:
        return None
