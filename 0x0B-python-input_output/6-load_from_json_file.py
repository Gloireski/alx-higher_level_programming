#!/usr/bin/python3
# 6-load_from_json_file.py
# Belem Gloire BEKOUTOU
"""define load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    Args:
        filename: file from which to create object
    """
    with open(filename, mode="r") as f:
        return json.load(f)
