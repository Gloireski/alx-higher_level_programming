#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        new_t = ""
        if ord(str[c]) >= ord('a') and ord(str[c]) <= ord('z'):
            asc = ord(str[c]) - 32
            new_t = chr(asc)
        else:
            new_t = str[c]
        print("{}".format(new_t), end='')
    print("")
