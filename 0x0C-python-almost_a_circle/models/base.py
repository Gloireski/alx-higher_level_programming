#!/usr/bin/python3
# Belem Gloire BEKOUTOU
"""define first class base"""
import json


class Base:
    """Base model

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
