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
        """Validates value
        Arguments:
            name {str} -- name of an instance
            value {int} -- type of instance
        Raises:
            TypeError: [must be an integer]
            ValueError: [must be greater than 0]
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
