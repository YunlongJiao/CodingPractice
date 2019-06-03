# NOTE
# Another example solved by sliding window technique!


def longest_substr_no_repeat(s):
    """
    3. Longest Substring Without Repeating Characters

    Given a string, find the length of the longest substring without repeating characters.

    https://leetcode.com/problems/longest-substring-without-repeating-characters/

    """

    begin, end, max_len = 0, 0, 0
    found = set()

    while end < len(s):
        while s[end] in found:
            found.remove(s[begin])
            begin += 1
        found.add(s[end])
        max_len = max(max_len, end - begin + 1)
        end += 1

    return max_len


if __name__ == '__main__':
    print(longest_substr_no_repeat("abcabcbb"))
    print(longest_substr_no_repeat("bbbbb"))
    print(longest_substr_no_repeat("pwwkew"))
