#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenarg = len(sys.argv)
    arg = sys.argv
    i = 2
    if len(sys.argv) == 1:
        print("{} argument.".format(0))
    elif len(sys.argv) == 2:
        print("{} argument:".format(lenarg - 1))
        print("{}: {}".format(1, arg[1]))
    else:
        print("{} arguments:".format(lenarg - 1))
        for i in range(1, lenarg):
            print("{}: {}".format(i, arg[i]))
