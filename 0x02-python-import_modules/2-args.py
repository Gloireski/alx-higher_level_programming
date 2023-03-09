#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    t = len(sys.argv)
    if t < 2:
        print("{:d} arguments.".format(t - 1))
    elif t == 2:
        print("{:d} arguments:".format(t - 1))
        print("{:d}: {:s}".format(t - 1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(t - 1))
        for c in range(1, t):
            print("{:d}: {:s}".format(c, sys.argv[c]))
