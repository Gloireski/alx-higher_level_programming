#!/usr/bin/python3
# 3-is_kind_of_class.py
"""
    File name : 3-is_kind_of_class.py
    Requirement: not allowed to import any module
"""


def is_kind_of_class(obj, a_class):
    """
        check is object is an instance of a class or subclass
    """
    if type(obj) == a_class:
        return True
    elif isinstance(obj, a_class):
        return True
    else:
        return False
