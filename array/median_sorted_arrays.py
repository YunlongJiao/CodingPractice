# NOTE
# While first solution is O(n) time and O(1) space, second is O(log n) time and O(1) space!


# def median_sorted_arrays(nums1, nums2):
#
#     arr = []
#     max_len = 1 if (len(nums1) + len(nums2)) % 2 else 2
#     count = 0
#     max_count = (len(nums1) + len(nums2)) // 2 + 1
#
#     idx1, idx2 = 0, 0
#     while count < max_count and idx1 < len(nums1) and idx2 < len(nums2):
#         if nums1[idx1] < nums2[idx2]:
#             arr.append(nums1[idx1])
#             idx1 += 1
#         else:
#             arr.append(nums2[idx2])
#             idx2 += 1
#         if len(arr) > max_len:
#             arr.pop(0)
#         count += 1
#
#     if count != max_count:
#         nums, idx = (nums1, idx1) if idx2 == len(nums2) else (nums2, idx2)
#         while count < max_count:
#             arr.append(nums[idx])
#             idx += 1
#             if len(arr) > max_len:
#                 arr.pop(0)
#             count += 1
#
#     return sum(arr)/len(arr)


def median_sorted_arrays(nums1, nums2):
    """
    4. Median of Two Sorted Arrays

    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    You may assume nums1 and nums2 cannot be both empty.

    https://leetcode.com/problems/median-of-two-sorted-arrays/

    This binary search solution was taken from
    https://leetcode.com/problems/median-of-two-sorted-arrays/solution/

    """

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # make sure num1 is the shorter array

    len1, len2 = len(nums1), len(nums2)  # len1 <= len2 guaranteed
    left, right, half_len = 0, len1, (len1 + len2 + 1)//2

    while left <= right:
        mid = (left + right) // 2
        rest = half_len - mid
        if mid < len1 and nums2[rest - 1] > nums1[mid]:
            # mid is too small, reset search by increasing it
            left = mid + 1
        elif mid > 0 and nums1[mid - 1] > nums2[rest]:
            # mid is too big, reset search by decreasing it
            right = mid - 1
        else:
            # mid is found
            break

    # max on left
    if mid == 0:
        max_of_left = nums2[rest - 1]
    elif rest == 0:
        max_of_left = nums1[mid - 1]
    else:
        max_of_left = max(nums1[mid - 1], nums2[rest - 1])

    # min on right
    if mid == len1:
        min_of_right = nums2[rest]
    elif rest == len2:
        min_of_right = nums1[mid]
    else:
        min_of_right = min(nums1[mid], nums2[rest])

    # median of two arrays
    if (len1 + len2) % 2 == 1:
        return max_of_left
    else:
        return (max_of_left + min_of_right) / 2.


if __name__ == '__main__':
    print(median_sorted_arrays([1, 3], [2]))
    print(median_sorted_arrays([1, 2], [3, 4]))
    print(median_sorted_arrays([1, 2], [-1, 3]))
