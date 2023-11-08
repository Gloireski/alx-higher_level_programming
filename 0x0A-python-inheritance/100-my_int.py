#!/usr/bin/python3
# 100-my_int.py
# Belem Gloire BEKOUTOU
"""define MyInt class"""


class MyInt(int):
    """custom int class"""

    def __init__(self, number):
        self.number = number

    def __eq__(self, x):
        """overloads == methods"""
        return not (self.number == x)

    def __ne__(self, x):
        """overloadds != method"""
        return not (self.number != x)
