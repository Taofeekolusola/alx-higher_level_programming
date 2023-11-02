#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # Print sorted name from directory
    for a in sorted(dir(hidden_4)):
        # print only names that do not start with __
        if a[:2] != '__':
            print("{}".format(a))
