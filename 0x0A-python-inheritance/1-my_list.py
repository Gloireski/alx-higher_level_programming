#!/usr/bin/python3
# 1-my_list.py
# Belem Gloire BEKOUTOU
"""Define MyList class"""


class MyList(list):
    """MyList class, inherits list"""
    pass


    def print_sorted(self):
        """prints the list, but sorted (asc sort)"""

        print(sorted(list(self)))
