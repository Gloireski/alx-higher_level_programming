#!/usr/bin/python3
# 2-is_same_class.py
# Belem Gloire BEKOUTOU
"""define is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False."""

    return isinstance(obj, a_class)
