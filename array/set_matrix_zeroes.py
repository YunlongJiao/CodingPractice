# NOTE
# The constant space solution uses first row/col to indicate flags instead of extra memory!
# Similarly to the idea of ../beginner/find_repeated.py


# # Method 1: O(n*n) time and O(m+n) space
# def set_matrix_zeroes(matrix):
#
#     nrow, ncol = len(matrix), len(matrix[0])
#     zrow = set()
#     zcol = set()
#
#     for i in range(nrow):
#         for j in range(ncol):
#             if matrix[i][j] == 0:
#                 zrow.add(i)
#                 zcol.add(j)
#
#     for i in zrow:
#         for j in range(ncol):
#             matrix[i][j] = 0
#     for j in zcol:
#         for i in range(nrow):
#             matrix[i][j] = 0
#
#     return


# Method 2: O(n*n) time and O(1) space
def set_matrix_zeroes(matrix):
    """
    73. Set Matrix Zeroes

    Given a m x n matrix, if an element is 0, set its entire row and column to 0.
    Do it in-place.

    https://leetcode.com/problems/set-matrix-zeroes/

    This solution is taken from
    https://leetcode.com/problems/set-matrix-zeroes/solution/

    """

    nrow, ncol = len(matrix), len(matrix[0])
    first_col_zero = 1
    for r in range(nrow):
        if matrix[r][0] == 0:
            first_col_zero = 0
        for c in range(1, ncol):  # skipping col 0
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for r in range(1, nrow):  # skipping col 0
        for c in range(1, ncol):  # skipping col 0
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:  # set row 0
        r = 0
        for c in range(ncol):
            matrix[r][c] = 0

    if first_col_zero == 0:  # set col 0
        c = 0
        for r in range(nrow):
            matrix[r][c] = 0

    return


if __name__ == '__main__':
    m1 = [
      [1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]
    ]
    set_matrix_zeroes(m1)
    print(m1)

    m2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    set_matrix_zeroes(m2)
    print(m2)

    m3 = [
        [1, 1, 1],
        [0, 1, 2]
    ]
    set_matrix_zeroes(m3)
    print(m3)
