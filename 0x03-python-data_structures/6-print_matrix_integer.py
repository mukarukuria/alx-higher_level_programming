#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for el in row:
            print("{}".format(el), end=" ")

        print()
