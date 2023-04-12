#!/usr/bin/python3
"""contains the MyList class"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """object initialization"""
        super().__init__()

    def print_sorted(self):
        """sorted list"""
        print(sorted(self))
