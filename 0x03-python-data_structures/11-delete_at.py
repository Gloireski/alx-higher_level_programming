#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    vidx = 0
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    vidx = my_list[idx]
    my_list.remove(vidx)
    return my_list
