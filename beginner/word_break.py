# NOTE:
# A bit more complicated to find all decompositions - much simpler if only asked existence Yes/No!


def wb(d, s, decomp, l):
    """
    Recursive implementation of complexity O(len(d) len(s))
    """

    if len(s) == 0:
        l.append(decomp)
        return True
    else:
        for item in d:
            if s.startswith(item):
                decomp_add = decomp + ' ' + item
                if wb(d, s[len(item):], decomp_add, l):
                    decomp = decomp_add
        return False


def word_break(d, s):
    """
    Given an input string and a dictionary of words,
    find out if the input string can be segmented into a space-separated sequence of dictionary words.

    https://www.geeksforgeeks.org/word-break-problem-dp-32/

    """

    l = []
    wb(d, s, '', l)
    for i in range(len(l)):
        l[i] = l[i][1:]
    return l


if __name__ == '__main__':

    d = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
    print(word_break(d, 'ilike'))
    print(word_break(d, 'ilikesamsung'))
    print(word_break(d, 'mangosamsungicecream'))
