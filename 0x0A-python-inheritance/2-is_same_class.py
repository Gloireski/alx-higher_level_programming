#!/usr/bin/python3
# 2-is_same_class.py
# Belem Gloire BEKOUTOU
"""define is_same function"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of
    the specified class ; otherwise False."""
    
    return isinstance(obj, a_class)
