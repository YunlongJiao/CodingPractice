# NOTE
# While the following implementation is O(n), a divide-and-conquer approach in O(n log n) is found at
# https://leetcode.com/problems/maximum-subarray/discuss/163139/solution-with-divide-and-conquer-as-well-as-normal-iterative-both-acccepted


def max_subarray(nums):
    """
    53. Maximum Subarray

    Given an integer array nums,
    find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    https://leetcode.com/problems/maximum-subarray/

    """

    s, m, best = 0, float('inf'), float('-inf')

    for i in nums:
        s += i  # accumulated sum
        best = max(s, s-m, best)
        m = min(s, m)  # minimum acc sum

    return best


if __name__ == '__main__':
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
