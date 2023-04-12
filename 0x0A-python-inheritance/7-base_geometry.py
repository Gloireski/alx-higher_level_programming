#!/usr/bin/python3
# 7-base_geometry.py
"""
    File name : 7-base_geometry.py
    Requirement: not allowed to import any module
"""


class BaseGeometry(object):
    """
        class BaseGeometry
    """
    def area(self):
        """
             raises an Exception with the message
             area() is not implemented
        """
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """
            validates value
        """
        if isinstance(value, int) == False:
            raise TypeError(name+" must be an integer")
        if value <= 0:
            raise ValueError(name+" must be greater than 0")
