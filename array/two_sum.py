# NOTE
# In Python, set or dict has O(1) lookup time! (While heapq has O(log n) insert time and O(1) retrieval of max element)


def two_sum(nums, target):
    """
    1. Two Sum
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    https://leetcode.com/problems/two-sum/

    """

    d = dict()

    for i, x in enumerate(nums):
        if target - x in d:
            return d[target-x], i
        elif x not in d:
            d[x] = i

    return -1


if __name__ == '__main__':
    print(two_sum([11, 2, 11, 7, 15], 9))
