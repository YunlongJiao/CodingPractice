# NOTE
# The first solution below is divide-and-conquer in time O(n log n) at memory consumption for memoisation!
# The second solution is O(n) similar to max_subarray.py!


# def memoise(f):
#     mem = {}
#
#     def memoised_f(arr, l, r):
#         key = tuple([*arr, l, r])
#         if key not in mem:
#             mem[key] = f(arr, l, r)
#         return mem[key]
#     return memoised_f
#
#
# @memoise
# def msp_util(arr, l, r):
#
#     if l > r:
#         return float('-inf')
#     else:
#         mid = (l+r)//2
#         if arr[mid] == 0:
#             best = 0
#         else:
#             max_low, max_high, min_low, min_high = 1, 1, 1, 1
#             acc_low, acc_high = 1, 1
#             low, high = mid-1, mid+1
#             while low >= l:
#                 acc_low *= arr[low]
#                 max_low = max(max_low, acc_low)
#                 min_low = min(min_low, acc_low)
#                 low -= 1
#             while high <= r:
#                 acc_high *= arr[high]
#                 max_high = max(max_high, acc_high)
#                 min_high = min(min_high, acc_high)
#                 high += 1
#             best = max(arr[mid] * max_high * max_low, arr[mid] * min_high * min_low,
#                        arr[mid] * max_high * min_low, arr[mid] * min_high * max_low)
#         return max(best, msp_util(arr, l, mid-1), msp_util(arr, mid+1, r))
#
#
# def max_subarray_product(nums):
#
#     return msp_util(nums, 0, len(nums)-1)


def max_subarray_product(nums):
    """
    152. Maximum Product Subarray
    Given an integer array nums,
    find the contiguous subarray within an array (containing at least one number) which has the largest product.

    https://leetcode.com/problems/maximum-product-subarray/

    """

    s, best = 1, float('-inf')
    pos_min, neg_max = float('inf'), float('-inf')

    for i in nums:
        s *= i  # accumulated sum
        this = s/pos_min if s >= 0 else float('-inf') if neg_max == float('-inf') else s/neg_max
        best = max(best, s, this)
        if s == 0:  # reinitialise
            s, pos_min, neg_max = 1, float('inf'), float('-inf')
        elif s > 0:
            pos_min = min(s, pos_min)
        else:
            neg_max = max(s, neg_max)

    return best


if __name__ == '__main__':
    print(max_subarray_product([2,3,-2,4]))
    print(max_subarray_product([-2,0,-1]))
    print(max_subarray_product([-4,-3]))
    print(max_subarray_product([2,-5,-2,-4,3]))
    print(max_subarray_product([-2]))
    print(max_subarray_product([-2, 2]))
    print(max_subarray_product([2, -2]))
    print(max_subarray_product([0, -2, 2]))
    print(max_subarray_product([0, 2, -2]))
