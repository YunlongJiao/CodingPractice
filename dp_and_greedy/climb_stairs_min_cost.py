# NOTE
# The first solution is recursion-based, still very slow even with memoisation!
# The second solution is DP-based non-recursive in time O(N) and space O(1)!


# def memoise(f):
#     mem = {}
#
#     def memoised_f(x, r):
#         key = tuple([*x, r])
#         if key not in mem:
#             mem[key] = f(x, r)
#         return mem[key]
#     return memoised_f
#
#
# @memoise
# def climb_util(cost, r):
#
#     if r < 1:
#         return 0
#     else:
#         return min(climb_util(cost, r-1) + cost[r], climb_util(cost, r-2) + cost[r-1])
#
#
# def climb_stairs_min_cost(cost):
#
#     return climb_util(cost, len(cost)-1)


def climb_stairs_min_cost(cost):
    """
    746. Min Cost Climbing Stairs

    On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
    Once you pay the cost, you can either climb one or two steps.
    You need to find minimum cost to reach the top of the floor,
    and you can either start from the step with index 0, or the step with index 1.

    https://leetcode.com/problems/min-cost-climbing-stairs/

    This solution is taken from
    https://leetcode.com/problems/min-cost-climbing-stairs/discuss/233486/Python-3%3A-Beat-99-Time-and-Space.-Easy-to-Understand-O(N)-time-and-O(1)-DP-Solution-with-Analysis

    """

    sum_include, sum_skip = 0, 0

    for c in reversed(cost):
        sum_include, sum_skip = c + min(sum_include, sum_skip), sum_include

    return min(sum_include, sum_skip)


if __name__ == '__main__':
    print(climb_stairs_min_cost([10, 15, 20]))
    print(climb_stairs_min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
