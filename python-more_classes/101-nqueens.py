#!/usr/bin/python3
"""Solves the N queens puzzle.

Determines all the possible solutions to placing N non-attacking
queens on an N×N chessboard.
"""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col) safely.

    Args:
        board (list): List where index is row and value is column
            of the queen placed in that row so far.
        row (int): Row to check.
        col (int): Column to check.

    Returns:
        bool: True if placing a queen at (row, col) is safe.
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Recursively find all solutions using backtracking.

    Args:
        n (int): Size of the board.
        row (int): Current row being processed.
        board (list): Current placement of queens by row.
        solutions (list): Accumulator for all found solutions.
    """
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(n, row + 1, board, solutions)
            board.pop()


def print_solutions(solutions):
    """Print all solutions in the required format.

    Args:
        solutions (list): List of solutions, each a list of columns
            indexed by row.
    """
    for solution in solutions:
        formatted = [[row, col] for row, col in enumerate(solution)]
        print(formatted)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    all_solutions = []
    solve_nqueens(n, 0, [], all_solutions)
    print_solutions(all_solutions)
