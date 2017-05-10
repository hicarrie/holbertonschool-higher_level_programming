#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("")
    for row in matrix:
        if len(row) == 0:
            print("")
        else:
            for i in range(len(row)):
                print("{:d}".format(row[i]), end="")
            print("")
