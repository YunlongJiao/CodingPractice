# NOTE
# The following solution is O(m*n) time, while O(m+n) time solution exists by KMP pattern matching
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/


def strStr(haystack, needle):
    """
    28. Implement strStr()

    Return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.

    For the purpose of this problem, we will return 0 when needle is an empty string.
    This is consistent to C's strstr() and Java's indexOf().

    https://leetcode.com/problems/implement-strstr/

    """

    nh = len(haystack)
    nn = len(needle)

    for i in range(nh-nn+1):
        if haystack[i:i+nn] == needle:
            return i

    return -1


if __name__ == '__main__':
    print(strStr("hello", "ll"))
    print(strStr("hello", ""))
    print(strStr("aaaaa", "bba"))
