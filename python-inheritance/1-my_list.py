#!/usr/bin/python3
"""
class MyList that inherits from list python-inheritance.1-my_list
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """
        This method will be print the list, but sorted ascending sort
        """
        lis = self.copy()
        lis.sort()
        return print(lis)
