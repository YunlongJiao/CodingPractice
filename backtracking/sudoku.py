# NOTE:
# General backtracking algorithm reference https://www.geeksforgeeks.org/backtracking-algorithms/


def print_sudoku(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()
    return


def is_num_valid(board, row, col, num):
    def _is_num_valid_row(board, row, col, num):
        for i in range(9):
            if board[row][i] == str(num):
                return False
        return True

    def _is_num_valid_col(board, row, col, num):
        for i in range(9):
            if board[i][col] == str(num):
                return False
        return True

    def _is_num_valid_box(board, row, col, num):
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == str(num):
                    return False
        return True

    return _is_num_valid_row(board, row, col, num) and \
        _is_num_valid_col(board, row, col, num) and \
        _is_num_valid_box(board, row, col, num)


def find_empty_cell(board, pos):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                pos[0] = i
                pos[1] = j
                return True
    return False


def solve_sudoku(board):
    """
    37. Sudoku Solver

    Write a program to solve a Sudoku puzzle by filling the empty cells.

    A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    The '.' character indicates empty cells.

    https://leetcode.com/problems/sudoku-solver/

    This solution is taken from
    https://www.geeksforgeeks.org/sudoku-backtracking-7/

    """
    pos = [0, 0]
    if not find_empty_cell(board, pos):
        # If already solved
        return True
    # Otherwise return the position of an empty cell
    row, col = pos

    # Try to solve the board
    for num in range(1, 10):
        if is_num_valid(board, row, col, num):
            # Fill the empty cell
            board[row][col] = str(num)
            if solve_sudoku(board):
                # Solve the board with one extra cell filled
                return True
            else:
                # Otherwise revert the cell just filled
                board[row][col] = '.'
    # Invoke backtracking
    return False


if __name__ == '__main__':
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    solve_sudoku(board)
    print_sudoku(board)
