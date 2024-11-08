#!/usr/bin/python3i
"""
This module provides a solution to the N Queens puzzle using backtracking. The puzzle consists of placing N queens on an N×N chessboard such that no two queens attack each other. The program will print every possible solution, one per line.

The module includes the following functions:
- print_board: Prints the current board state with queens placed.
- is_safe: Checks if it is safe to place a queen at a given position.
- solve_nqueens: Recursively solves the N Queens problem using backtracking.
- nqueens: Initiates the solving process and handles input validation.
"""
import sys


def print_board(board):
    """Print the chessboard with queens placed on it.
    
    Args:
        board (list of list of int): The current state of the board
        where 1 represents a queen and 0 represents an empty space.
    """
    for row in board:
        # Print each row with 'Q' for queen and '.' for an empty space
        print("".join("Q" if x == 1 else "." for x in row))


def is_safe(board, row, col, N):
    """Check if placing a queen at board[row][col] is safe from other queens.
    
    Args:
        board (list of list of int): The current state of the board.
        row (int): The row where the queen is to be placed.
        col (int): The column where the queen is to be placed.
        N (int): The size of the board (N x N).
    
    Returns:
        bool: True if it is safe to place a queen, False otherwise.
    """
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check the upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check the upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j] == 1:
            return False
    
    return True


def solve_nqueens(board, row, N):
    """Recursively solve the N Queens problem using backtracking.
    
    Args:
        board (list of list of int): The current state of the board.
        row (int): The current row being filled with a queen.
        N (int): The size of the board (N x N).
    
    Returns:
        bool: True if a solution is found, False if no solution exists.
    """
    # If we've placed queens in all rows, print the board and return True
    if row == N:
        print_board(board)
        return True
    
    res = False
    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place a queen
            res = solve_nqueens(board, row + 1, N) or res  # Recurse for next row
            board[row][col] = 0  # Backtrack
    
    return res


def nqueens(N):
    """Solve the N Queens problem.
    
    Args:
        N (int): The size of the chessboard and the number of queens.
    
    Raises:
        SystemExit: If the input is invalid or no solution is found.
    """
    # Validate that N is an integer and at least 4
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize the chessboard with all zeros (empty spaces)
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # Start solving the puzzle from the first row
    if not solve_nqueens(board, 0, N):
        print("No solution exists")
        sys.exit(1)


def main():
    """Main function to handle user input and solve the N Queens problem.
    
    It checks if the correct number of arguments is provided and
    handles errors.
    """
    # Ensure the program is called with exactly one argument (N)
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])  # Convert the argument to an integer
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Solve the N Queens problem with the given N
    nqueens(N)

if __name__ == "__main__":
    main()
