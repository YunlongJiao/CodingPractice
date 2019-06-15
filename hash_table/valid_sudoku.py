# NOTE


def valid_sudoku_util(board, rows, cols):

    numbers = set()

    for r in rows:
        for c in cols:
            digit = board[r][c]
            if digit != '.' and digit in numbers:
                return False
            else:
                numbers.add(board[r][c])

    return True


def valid_sudoku(board):
    """
    36. Valid Sudoku

    Determine if a 9x9 Sudoku board is valid.
    Only the filled cells need to be validated according to the following rules:
    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

    Note:
    - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    - Only the filled cells need to be validated according to the mentioned rules.
    - The given board contain only digits 1-9 and the character '.'.
    - The given board size is always 9x9.

    https://leetcode.com/problems/valid-sudoku/

    """

    is_valid = True

    for i in range(9):
        is_valid = is_valid and \
                   valid_sudoku_util(board, [i], list(range(9))) and \
                   valid_sudoku_util(board, list(range(9)), [i])

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            is_valid = is_valid and \
                       valid_sudoku_util(board, list(range(r, r+3)), list(range(c, c+3)))

    return is_valid


if __name__ == '__main__':
    board1 = [
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
    print(valid_sudoku(board1))

    board2 = [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    print(valid_sudoku(board2))
