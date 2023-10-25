#!/usr/bin/python3
# 3-safe_print_division.py
# Belem Gloire BEKOUTOU 

def safe_print_division(a, b):
    """Returns the result of the divison of a by b"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return(result)
