#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    b = 1
    for i in range(len(matrix)):
        if i == b:
            print(end="\n")
            b += 1
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end=" ")
    print("", end="\n")
