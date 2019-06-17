# NOTE


from itertools import cycle, chain


def spiral_order_util(matrix, ij, m, n, ans):

    if m > 0 or n > 0:
        iterations = chain(
            zip(cycle([0]), range(n)),
            zip(range(1, m), cycle([n-1])),
            zip(cycle([m-1]), range(n-2, -1, -1)) if m > 1 else zip(),
            zip(range(m-2, 0, -1), cycle([0])) if n > 1 else zip(),
        )
        for i, j in iterations:
            ans.append(matrix[ij + i][ij + j])

    return


def spiral_order(matrix):
    """
    54. Spiral Matrix

    Given a matrix of m x n elements (m rows, n columns),
    return all elements of the matrix in spiral order.

    https://leetcode.com/problems/spiral-matrix/

    """

    ans = []
    ij, m, n = 0, len(matrix), len(matrix[0]) if len(matrix) > 0 else 0

    while m > 0 and n > 0:
        spiral_order_util(matrix, ij, m, n, ans)
        ij += 1
        m -= 2
        n -= 2

    return ans


if __name__ == '__main__':
    m1 = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    print(spiral_order(m1))

    m2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(spiral_order(m2))
