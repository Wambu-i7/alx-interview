#!/usr/bin/python3
"""
An implementation of a rotated 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    Generate a rotated 2d matrix
    # Assumption: n is always an integer
    """
    n = len(matrix)
    
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
