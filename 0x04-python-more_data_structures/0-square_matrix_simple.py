#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) == int:
                new_matrix[i].append(matrix[i][j] ** 2)
            else:
                new_matrix[i].append(matrix[i][j])

    return new_matrix
