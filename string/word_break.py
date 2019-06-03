# NOTE:
# This is to only output True/False decomposable, as compared to ../string/word_break.py


def memoise(f):
    mem = {}

    def memoised_f(s, d):
        key = tuple([s, *d])
        if key not in mem:
            mem[key] = f(s, d)
        return mem[key]

    return memoised_f


@memoise
def word_break(s, wordDict):

    """
    139. Word Break

    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
    determine if s can be segmented into a space-separated sequence of one or more dictionary words.
    Note:
    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

    https://leetcode.com/problems/word-break/

    """

    if len(s) == 0:
        return True
    else:
        flag = False
        for item in wordDict:
            if s.startswith(item) and word_break(s[len(item):], wordDict):
                flag = True
        return flag


if __name__ == '__main__':

    d = ['car', 'ca', 'rs']
    print(word_break('cars', d))

    d = ['a']
    print(word_break('a', d))
