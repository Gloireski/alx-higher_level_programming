#!/usr/bin/python3
for nb in range(0, 99):
    if nb < 98:
        print("{:02d}, ".format(nb), end=' ')
    else:
        print(nb)
