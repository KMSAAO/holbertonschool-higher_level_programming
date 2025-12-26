#!/usr/bin/python3
"""
This module provides a VerboseList class that notifies
the user of modifications to the list.
"""


class VerboseList(list):
    """A list subclass that prints a message for every modification."""
    def append(self, item):
        super().append(item)

        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index=-1):
        the_popped = super().pop(index)
        print(f"Popped [{the_popped}] from the list.")
        return the_popped
