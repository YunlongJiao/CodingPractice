# NOTE


def search_rotated_array(nums, target):
    """
    33. Search in Rotated Sorted Array

    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
    You are given a target value to search. If found in the array return its index, otherwise return -1.
    You may assume no duplicate exists in the array.
    Your algorithm's runtime complexity must be in the order of O(log n).

    https://leetcode.com/problems/search-in-rotated-sorted-array/

    """

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == '__main__':
    print(search_rotated_array([4,5,6,7,0,1,2], 0))
    print(search_rotated_array([4,5,6,7,0,1,2], 3))
    print(search_rotated_array([3,1], 1))
