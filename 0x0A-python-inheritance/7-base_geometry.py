#!/usr/bin/python3
# 7-base_geometry.py
# Belem Gloire BEKOUTOU
"""define class base on BaseGeometry"""


class BaseGeometry(object):
    """BaseGeometry based class"""
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
