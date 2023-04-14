#!/usr/bin/python3
# 0-add_integer.py
"""
    not allowed to import any module
"""


def add_integer(a, b=98):
    """
        sum a and b
    """
    if (a is None or (type(a) is not int) and (type(a) is not float)):
        raise TypeError("a must be an integer")
    if ((type(b) is not int) and (type(b) is not float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
