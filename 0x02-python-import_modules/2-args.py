#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    size = len(args) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for a in range(1, size + 1):
            print("{}: {}".format(a, args[a]))

    elif size == 0:
        print("{} arguments.".format(size))

    else:
        print("{} argument:".format(size))
        print("{}: {}".format(size, args[1]))
#prints the number of and the list of its arguments
