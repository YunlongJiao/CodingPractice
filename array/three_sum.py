# NOTE
# The second solution is still O(n log n + 0.5 n**2), suppose there is no O(n log n) or O(n) solution?


# def two_sum(nums, target, id, sums):
#
#     d = dict()
#
#     for i, x in enumerate(nums):
#         if i == id:
#             continue
#         if target - x in d:
#             sums.add(tuple(sorted([target - x, x, -target])))
#         elif x not in d:
#             d[x] = i
#
#     return -1
#
# def three_sum(nums):
#
#     sums = set()
#     visited = set()
#     for i, x in enumerate(nums):
#         if x not in visited:
#             two_sum(nums, -x, i, sums)
#             visited.add(x)
#     sums = list(map(list, sums))
#     return sums


def three_sum(nums):
    """
    15. 3Sum

    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.
    The solution set must not contain duplicate triplets.

    https://leetcode.com/problems/3sum/

    This solution was taken from https://leetcode.com/problems/3sum/discuss/7652/Python-solution-196ms

    """

    nums.sort()
    i, n, sums = 0, len(nums), []

    while i < n-2:
        j, k = i+1, n-1

        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if not s:
                sums.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif s > 0:
                k -= 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            else:
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
        i += 1
        while i < n-2 and nums[i] == nums[i-1]:
            i += 1

    return sums


if __name__ == '__main__':
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(three_sum([-1, 0, 1, 0]))
    print(three_sum([-2, 0, 1, 1, 2]))
