#!/usr/bin/python3
# 2-is_same_class.py
"""
    File name : 2-is_same_class.py
    Requirement: not allowed to import any module
"""


def is_same_class(obj, a_class):
    """
        check is object is an instance of a class
    """
    r = isinstance(obj, a_class)
    return r
