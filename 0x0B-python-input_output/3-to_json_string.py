#!/usr/bin/python3
# 3-to_json_string.py
# Belem Gloire BEKOUTOU
"""define to_json_string function"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
        my_obj: object to serialize

    Return: JSON rep of my_obj
    """
    return json.dumps(my_obj)
