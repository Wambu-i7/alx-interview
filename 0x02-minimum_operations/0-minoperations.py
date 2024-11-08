#!/usr/bin/python3
"""
Module: min_operations

This module provides a function to calculate the minimum number of operations
needed to reach exactly 'n' 'H' characters in a text file.
"""


def minOperations(n):
    """
    Returns the fewest operations needed to get exactly 'n' 'H' characters in a
    file, starting from one 'H'.

    Parameters:
    n (int): Target number of 'H' characters.

    Returns:
    int: Minimum number of operations to reach 'n' characters, or 0 if n <= 1.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
