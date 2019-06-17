# NOTE
# Greedy algorithm should be fast without memoisation, which in turn sacrifices memory!


# # Method 1: Greedy algorithm implemented as top-down DP
# def jump_game_util(nums, n, pos):
#
#     if nums[pos] + pos >= n - 1:
#         # Can jump to the last position already
#         return True
#     else:
#         # Greedily search for the maximum jump steps ahead
#         best_step_ahead = 0
#         best_steps = nums[pos + best_step_ahead] + best_step_ahead
#         for step_ahead in range(nums[pos], 0, -1):
#             if nums[pos + step_ahead] + step_ahead >= best_steps:
#                 best_step_ahead = step_ahead
#                 best_steps = nums[pos + step_ahead] + step_ahead
#         if best_steps >= n - 1 - pos:
#             # Can jump to the last position at the maximum jump steps ahead
#             return True
#         elif best_steps == 0:
#             # Stuck at the current position
#             return False
#         else:
#             # Try jump
#             return jump_game_util(nums, n, pos + best_step_ahead)
#
#
# def jump_game(nums):
#
#     return jump_game_util(nums, len(nums), 0)


# Method 2: Greedy algorithm with efficient bottom-up update
def jump_game(nums):
    """
    55. Jump Game

    Given an array of non-negative integers,
    you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.

    https://leetcode.com/problems/jump-game/

    This solution is converted from the Greedy Approach (Java):
    https://leetcode.com/problems/jump-game/solution/

    """

    n = len(nums)

    last_pos = n - 1
    for pos in range(n-1, -1, -1):
        if nums[pos] + pos >= last_pos:
            last_pos = pos

    return last_pos == 0


if __name__ == '__main__':
    print(jump_game([2,3,1,1,4]))
    print(jump_game([3,2,1,0,4]))
    print(jump_game([1,2,3]))
    print(jump_game([4,2,0,0,1,1,4,4,4,0,4,0]))
