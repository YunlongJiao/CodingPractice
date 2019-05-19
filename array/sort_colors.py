# NOTE
# This is essentially equiv to the core step in a quick sort!


def sort_colors(nums):
    """
    75. Sort Colors
    Given an array with n objects colored red, white or blue, sort them in-place,
    so that objects of the same color are adjacent, with the colors in the order red, white and blue.
    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

    https://leetcode.com/problems/sort-colors/

    """

    idx0, idx1, idx2 = 0, 0, len(nums)-1

    while idx1 <= idx2:
        if nums[idx1] == 0:
            nums[idx0], nums[idx1] = nums[idx1], nums[idx0]
            idx1 += 1
            idx0 += 1
        elif nums[idx1] == 1:
            idx1 += 1
        elif nums[idx1] == 2:
            nums[idx2], nums[idx1] = nums[idx1], nums[idx2]
            idx2 -= 1  # do NOT increment idx1 in this case!!
        else:
            raise ValueError

    return


if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    sort_colors(nums)
    print(nums)

    nums = [1,2,0]
    sort_colors(nums)
    print(nums)

    nums = [2,0,1]
    sort_colors(nums)
    print(nums)

    nums = [1, 2, 0, 0]
    sort_colors(nums)
    print(nums)
