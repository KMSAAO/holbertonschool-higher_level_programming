#!/usr/bin/python3
"""
This module provides a CountedIterator class that tracks
the number of items iterated over.
"""


class CountedIterator:
    """
    An iterator wrapper that counts how many items have been fetched.
    """
    def __init__(self, data):
        """Initializes the iterator and sets the counter to zero."""
        self.__iterator = iter(data)
        self.__count = 0

    def __next__(self):
        """Fetches the next item and increments the counter."""
        item = next(self.__iterator)
        self.__count += 1
        return item

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def get_count(self):
        """Returns the current number of items iterated over."""
        return self.__count
