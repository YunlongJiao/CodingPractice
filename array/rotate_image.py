# NOTE


def rotate_image_util(matrix, ij, r):
    # Rotate the boundary of the sub-matrix matrix[ij:ij+r+1][ij:ij+r+1],
    # namely the frame consisting of the intersection of two rows (ij and ij+r) and two cols (ij and ij+r)

    if r >= 1:
        for k in range(r):
            # Rotate 4-tuple (0,k,r,r-k)+ij by forming adjacent pairs
            matrix[k+ij][r+ij], matrix[r+ij][r-k+ij], matrix[r-k+ij][ij], matrix[ij][k+ij] = matrix[ij][k+ij], matrix[k+ij][r+ij], matrix[r+ij][r-k+ij], matrix[r-k+ij][ij]
    return


def rotate_image(matrix):
    """
    48. Rotate Image

    You are given an n x n 2D matrix representing an image.
    Rotate the image by 90 degrees (clockwise).
    Note: You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
    DO NOT allocate another 2D matrix and do the rotation.

    https://leetcode.com/problems/rotate-image/

    """

    ij, r = 0, len(matrix)-1

    while r > 0:
        rotate_image_util(matrix, ij, r)
        ij += 1
        r -= 2

    return


if __name__ == '__main__':
    matrix1 = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    rotate_image(matrix1)
    print(matrix1)

    matrix2 = [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ]
    rotate_image(matrix2)
    print(matrix2)
