# NOTE


from collections import Counter


def min_window(s, t):
    """
    76. Minimum Window Substring
    Given a string S and a string T,
    find the minimum window in S which will contain all the characters in T in complexity O(n).

    https://leetcode.com/problems/minimum-window-substring/

    """

    n = len(s)
    begin, end = 0, 0  # sliding window [begin , end]
    best, d = 0, n  # best window [best : best+d+1)

    desire = Counter(t)  # counts required according to t
    total = len(desire)  # total number of unique char in t
    window = dict.fromkeys(desire.keys(), 0)  # counts in sliding window
    found = 0  # number of char with enough counts in sliding window

    while end < n:
        if s[end] in desire:
            window[s[end]] += 1
            if window[s[end]] == desire[s[end]]:
                found += 1

        while begin <= end and found == total:
            if s[begin] in desire:
                if end - begin < d:
                    d = end - begin
                    best = begin
                window[s[begin]] -= 1
                if window[s[begin]] < desire[s[begin]]:
                    found -= 1
            begin += 1  # shrinking begin inwards

        end += 1  # expanding end outwards

    return '' if d == n else s[best:(best+d+1)]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(min_window(s, t))
    print(min_window('a','aa'))
    print(min_window('aa','aa'))
