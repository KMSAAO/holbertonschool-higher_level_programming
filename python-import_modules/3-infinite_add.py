#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv
    a = 0
    for i in range(1, len(arg)):
        a += int(arg[i])

    print(a, end="\n")
