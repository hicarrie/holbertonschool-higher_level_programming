#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count < 2:
        if count == 0:
            print("{:d} argument.".format(count))
        if count == 1:
            print("{:d} argument:".format(count))
            print("{:s}".format(sys.argv[count]))
    else:
        print("{:d} arguments:".format(count))
        for i in range(1, count + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
