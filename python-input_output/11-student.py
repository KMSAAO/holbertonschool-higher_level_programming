#!/usr/bin/python3
"""
This file include class Student
"""


class Student():
    """
    This is a class for Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            new_dict = {}
            for j in attrs:
                if j in self.__dict__:
                    new_dict[j] = self.__dict__[j]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            self.__dict__[key] = json[key]
        return self.__dict__
