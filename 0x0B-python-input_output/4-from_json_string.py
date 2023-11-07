#!/usr/bin/python3
# 4-from_json_string.py
# Belem Gloire BEKOUTOU
"""define from_json_string"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string:

    Args:
        my_str: string to deserialize

    Return:
        object from string serialization
    """
    return json.loads(my_str)
