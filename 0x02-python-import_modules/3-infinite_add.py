#!/usr/bin/python3
def add_arg(argv):
    num = len(argv) - 1
    if num == 0:
        print("{:d}".format(num))
        return
    else:
        a = 1
        add = 0
        while a <= num:
            add += int(argv[a])
            a += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
