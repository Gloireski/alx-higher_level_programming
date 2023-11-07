#!/usr/bin/python3
# 5-save_to_json_file.py
# Belem Gloire BEKOUTOU
"""define save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to write
        filename: file to write on
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
