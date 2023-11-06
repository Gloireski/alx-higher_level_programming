#!/usr/bin/python3
# 2-is_same_class.py
# Belem Gloire BEKOUTOU
"""defines inheerit"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False."""

    return False if type(obj) is a_class else isinstance(obj, a_class)
