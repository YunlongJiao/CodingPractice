# NOTE
# The following solution is O(n**2) time and O(1) space, but the use of math.floor and math.ceil is slow..
# See an equiv but much more efficient implementation at
# https://leetcode.com/problems/longest-palindromic-substring/discuss/273315/Python-O(N2)-Expand-from-Center
# Standard DP solution with O(n**2) time and O(n**2) space can be found at
# https://leetcode.com/problems/longest-palindromic-substring/solution/
# Linear time solution with O(n) time and O(1) space can be found at
# https://leetcode.com/problems/longest-palindromic-substring/discuss/3190/11-line-Python-solution-112ms


import math


def longest_palindromic(s):
    """
    5. Longest Palindromic Substring

    Given a string s, find the longest palindromic substring in s.
    You may assume that the maximum length of s is 1000.

    https://leetcode.com/problems/longest-palindromic-substring/

    """

    n = len(s)
    best_left = 0
    best_right = 0

    for pos in range(2 * n - 1):
        for r in range(n):
            left = int(math.floor(pos/2. - r))
            right = int(math.ceil(pos/2. + r))
            if left >= 0 and right < n and s[left] == s[right] and right-left > best_right-best_left:
                best_left = left
                best_right = right
            if left < 0 or right >= n or s[left] != s[right]:
                break

    return s[best_left:best_right+1]


if __name__ == '__main__':
    print(longest_palindromic("babad"))
    print(longest_palindromic("cbbd"))
