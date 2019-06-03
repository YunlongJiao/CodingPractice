# NOTE
# This array problem is indeed an example of dynamic programming!
# This solution is O(n**2), while there exists O(n log n) solution using binary search! See
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74903/O(nlogn)-and-O(n2)-concise-solutions-in-Python-with-explanation


def longest_increasing_subseq(nums):
    """
    300. Longest Increasing Subsequence

    Given an unsorted array of integers, find the length of longest increasing subsequence.

    https://leetcode.com/problems/longest-increasing-subsequence/

    """

    n = len(nums)
    if n == 0:
        return 0

    max_lens = [0]*n

    for left in range(n-1, -1, -1):
        temp_len = 1
        for right in range(left+1, n):
            if nums[right] > nums[left]:
                temp_len = max(temp_len, max_lens[right]+1)
        max_lens[left] = temp_len

    return max(max_lens)


if __name__ == '__main__':
    print(longest_increasing_subseq([10,9,2,5,3,7,101,18]))
    print(longest_increasing_subseq([10,9,2,5,3,4]))
