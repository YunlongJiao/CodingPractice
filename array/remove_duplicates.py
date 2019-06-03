# NOTE
# Since matters not what is left beyond the returned length, avoid time-consuming del list!


# def remove_duplicates(nums):
#
#     left, right, n = 0, 1, len(nums)
#
#     while right < n:
#         while right < n and nums[right] == nums[right-1]:
#             right += 1
#         del nums[left+1:right]
#         left, right, n = left + 1, left + 2, len(nums)
#
#     return n


def remove_duplicates(nums):
    """
    26. Remove Duplicates from Sorted Array

    Given a sorted array nums, remove the duplicates in-place
    such that each element appear only once and return the new length.
    Do not allocate extra space for another array,
    you must do this by modifying the input array in-place with O(1) extra memory.
    It doesn't matter what you leave beyond the returned length.

    https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    This solution (converted from Java) is taken from
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/

    """

    if len(nums) == 0:
        return 0

    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == '__main__':
    nums = [1,1,2]
    print(remove_duplicates(nums))
    print(nums)

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(remove_duplicates(nums))
    print(nums)

    nums = [1,1]
    print(remove_duplicates(nums))
    print(nums)
