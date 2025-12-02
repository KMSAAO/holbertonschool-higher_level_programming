#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenarg = len(sys.argv)
    arg = sys.argv
    i = 2
    if len(sys.argv) == 1:
        print("{} argument.".format(0))
    else:
        print("{} argument:".format(lenarg - 1))
        for i in range(1, lenarg):
            print("{}: {}".format(i, arg[i]))
