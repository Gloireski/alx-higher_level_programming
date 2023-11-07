#!/usr/bin/python3
# 7-base_geometry.py
# Belem Gloire BEKOUTOU
"""define class base on BaseGeometry"""


class BaseGeometry(object):
    """BaseGeometry based class"""
    pass

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
