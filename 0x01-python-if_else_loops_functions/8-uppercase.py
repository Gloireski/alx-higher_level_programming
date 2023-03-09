#!/usr/bin/python3
def uppercase(str):
    if str == "":
        return ""
    for c in range(len(str)):
        if ord(str[c]) >= ord('a') and ord(str[c]) <= ord('z'):
            asc = ord(str[c]) - 32
        else:
            asc = ord(str[c])
        if c == len(str)-1:
            print("{}".format(chr(asc)))
        else:
            print("{}".format(chr(asc)), end='')
