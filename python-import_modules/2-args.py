#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    n = len(args)
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
        print("1: {}".format(args[0]))
    else:
        print("{} arguments:".format(n))
        for i, arg in enumerate(args):
            print("{}: {}".format(i + 1, arg))
