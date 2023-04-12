#!/usr/bin/python3
"""Attr lookup"""

def lookup(obj):
    """Lookup all attributes in Class
    Args:
        obj: class object
    Returns:
        nothing
    """
    return [i for i in dir(obj)]
