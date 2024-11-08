#!/usr/bin/python3
"""
This module generates Pascal's triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows.

    Pascal's triangle is a triangular array where each entry is the sum of
    the two entries directly above it in the previous row. The triangle
    begins with a single '1' at the top and has n rows.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list of lists: A list of lists of integers, where each inner list
                       represents a row in Pascal's triangle.
                       Returns an empty list if n <= 0.

    Examples:
        >>> pascal_triangle(1)
        [[1]]

        >>> pascal_triangle(5)
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    """
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Loop to generate each row from the second up to the nth row
    for i in range(1, n):
        # Start each row with 1
        row = [1]


        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # End each row with 1
        row.append(1)

        # Add the completed row to the triangle
        triangle.append(row)

    return triangle
