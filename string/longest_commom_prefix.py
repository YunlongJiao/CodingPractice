# NOTE


def longest_common_prefix(strs):
    """
    14. Longest Common Prefix
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    All given inputs are in lowercase letters a-z.

    https://leetcode.com/problems/longest-common-prefix/

    """

    prefix = ''

    for i in zip(*strs):
        if len(set(i)) == 1:
            prefix += i[0]
        else:
            break

    return prefix


if __name__ == '__main__':
    print(longest_common_prefix(["flower","flow","flight"]))
    print(longest_common_prefix(["dog","racecar","car"]))
