# NOTE
# The first solution is a O(N) time and O(N) space solution, while second uses two pointers to reduce to O(1) space!


# def trapping_water(height):
#
#     max_from_left = []
#     left = 0
#     for h in height:
#         left = max(left, h)
#         max_from_left.append(left)
#
#     max_from_right = []
#     right = 0
#     for h in reversed(height):
#         right = max(right, h)
#         max_from_right.insert(0, right)
#
#     water = 0
#     for h, left, right in zip(height, max_from_left, max_from_right):
#         water += min(left, right) - h  # water at height h = min(max_from_left, max_from_right) - height
#
#     return water


def trapping_water(height):
    """
    42. Trapping Rain Water
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it is able to trap after raining.

    https://leetcode.com/problems/trapping-rain-water/

    This solution is taken from
    https://leetcode.com/problems/trapping-rain-water/discuss/245162/Python-easy-to-understand-solution-one-pass-using-2-pointers

    """

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0

    while left <= right:
        if left_max < right_max:
            left_max = max(left_max, height[left])
            water += left_max - height[left]  # min(left_max, right_max) = left_max at height[left] guaranteed
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]  # min(left_max, right_max) = right_max at height[right] guaranteed
            right -= 1

    return water


if __name__ == '__main__':
    print(trapping_water([0,1,0,2,1,0,1,3,2,1,2,1]))
