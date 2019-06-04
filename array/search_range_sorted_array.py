# NOTE
# First solution is O(n) while second is O(log n) as required!


# # Method 1: linear search
# def search_range_sorted_array(nums, target):
#
#     begin, end = -1, -1
#     for i, n in enumerate(nums):
#         if n == target:
#             end = i
#             if begin == -1:
#                 begin = i
#         if end != -1 and n != target:
#             break
#
#     return [begin, end]


# Method 2: binary search (twice)
def search_range_sorted_array(nums, target):
    """
    34. Find First and Last Position of Element in Sorted Array

    Given an array of integers nums sorted in ascending order,
    find the starting and ending position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].

    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

    """

    n = len(nums)
    begin, end = -1, -1
    begin_left, begin_right = 0, n-1
    end_left, end_right = 0, n-1

    while begin_left <= begin_right:
        mid = (begin_left + begin_right) // 2
        if nums[mid] > target:
            begin_right = mid - 1
        elif nums[mid] < target:
            begin_left = mid + 1
        else:
            if mid == 0 or nums[mid - 1] < target:
                begin = mid
                break
            else:
                begin_right = mid - 1

    while end_left <= end_right:
        mid = (end_left + end_right) // 2
        if nums[mid] > target:
            end_right = mid - 1
        elif nums[mid] < target:
            end_left = mid + 1
        else:
            if mid == n-1 or nums[mid + 1] > target:
                end = mid
                break
            else:
                end_left = mid + 1

    return [begin, end]


if __name__ == '__main__':
    print(search_range_sorted_array([5,7,7,8,8,10], 8))
    print(search_range_sorted_array([5,7,7,8,8,10], 6))
    print(search_range_sorted_array([2,2], 2))
