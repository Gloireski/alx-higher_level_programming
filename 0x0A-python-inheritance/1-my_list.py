#!/usr/bin/python3
# 1-my_list.py
"""
    File name : 1-my_list.py
    Requirement: not allowed to import any module
"""


class MyList(list):
    """
        MyList that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))
