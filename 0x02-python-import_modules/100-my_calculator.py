#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    nargs = len(sys.argv)
    if nargs != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    a, b = int(sys.argv[1]), int(sys.argv[3])
    if op == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
    elif op == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
    elif op == "*":
        print("{:d} {:c} {:s} = {:d}".format(a, op, b, mul(a, b)))
    elif op == "/":
        print("{:d} {:c} {:s} = {:d}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
