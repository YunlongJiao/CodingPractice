# NOTE
# Remember first thing to do in bottom-up DP solution is to create the n**2 matrix to save the solution path!


def regex_match(s, p):
    """
    10. Regular Expression Matching

    Given an input string (s) and a pattern (p), implement regular expression matching,
    with support for '.' (any single char) and '*' (zero or more of the preceding char).
    The matching should cover the entire input string (not partial).
    Return "true" if match or "false" if not match.

    Note:
    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like . or *.

    https://leetcode.com/problems/regular-expression-matching/

    This bottom-up DP solution is taken from
    https://leetcode.com/problems/regular-expression-matching/solution/
    See also top-down DP solution with memoisation!

    """

    ns = len(s)
    np = len(p)

    # Create DP solution matrix of entry [i][j] records whether s[i:] matches p[j:] for i<=len(s), j<=len(p)
    is_match = [[False] * (np + 1) for _ in range(ns + 1)]
    is_match[-1][-1] = True  # in row [-1], only column [-1] is true

    for i in range(ns, -1, -1):
        for j in range(np-1, -1, -1):  # in row [-1], only column [-1] is true
            this_match = i < ns and (s[i] == p[j] or p[j] == '.')
            if j+1 < np and p[j+1] == '*':
                is_match[i][j] = is_match[i][j+2] or (this_match and is_match[i+1][j])
            else:
                is_match[i][j] = this_match and is_match[i+1][j+1]

    return is_match[0][0]


if __name__ == '__main__':
    print(regex_match("abc", "a.c"))
    print(regex_match("aa", "a"))
    print(regex_match("a", "aa"))
    print(regex_match("a", "a*b*"))
    print(regex_match("aa", "a*"))
    print(regex_match("ab", ".*"))
    print(regex_match("aab", "c*a*b"))
    print(regex_match("mississippi", "mis*is*p*."))
    print(regex_match("abcd", "d*"))
    print(regex_match("aaa", "a*a"))
