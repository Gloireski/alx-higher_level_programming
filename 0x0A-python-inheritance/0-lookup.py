#!/usr/bin.python3
# 0-lookup.py
# Belem Gloire BEKOUTOU
"""Define lookup function"""


def lookup(obj):
    """
    Returns  list of available attributes and
    methods of an object.

    Args:
        object: object of which to returns attr and meth
    """
    return dir(obj)
