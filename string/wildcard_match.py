# NOTE
# See a similar problem of regex match in ./regex_match.py
# Notably, the order of j preceding i in the nested loop is essential for the correct wildcard any_match!


def wildcard_match(s, p):
    """
    44. Wildcard Matching

    Given an input string (s) and a pattern (p),
    implement wildcard pattern matching with support for '?' and '*'.

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    The matching should cover the entire input string (not partial).
    Return True if match or False if not match.

    Note:
    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.

    https://leetcode.com/problems/wildcard-matching/

    """

    ns, np = len(s), len(p)
    is_match = [[False] * (np + 1) for _ in range(ns + 1)]
    is_match[-1][-1] = True

    for j in range(np - 1, -1, -1):
        any_match = False  # any of s[i:], s[i+1:], s[i+2], ... matches with any p[j+1:] when p[j]=='*'
        for i in range(ns, -1, -1):
            any_match = any_match or is_match[i][j+1]
            if p[j] == '*':
                is_match[i][j] = any_match
            else:
                this_match = i < ns and (s[i] == p[j] or p[j] == '?')
                is_match[i][j] = this_match and is_match[i+1][j+1]

    return is_match[0][0]


if __name__ == '__main__':
    print(wildcard_match("aa", "a"))
    print(wildcard_match("aa", "*"))
    print(wildcard_match("cb", "?a"))
    print(wildcard_match("adceb", "*a*b"))
    print(wildcard_match("acdcb", "a*c?b"))
