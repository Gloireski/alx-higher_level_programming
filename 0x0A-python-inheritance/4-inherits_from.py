#!/usr/bin/python3
# 4-inherits_from.py
"""
    File name : 4-inherits_from.py
    Requirement: not allowed to import any module
"""


idef inherits_from(obj, a_class):
    """
        check is object is an instance of a class or subclass
        directly or not
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
