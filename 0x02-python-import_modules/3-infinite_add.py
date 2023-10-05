#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    t = len(sys.argv)
    s = 0
    if t > 1:
        for c in range(1, t):
            s = s + int(sys.argv[c])
    print("{}".format(s))
