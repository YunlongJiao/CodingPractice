# NOTE
# First solution does not depend on any library, while second is more concise by using itertools.groupby


def memoise(f):
    mem = {}

    def memoised_f(n):
        if n not in mem:
            mem[n] = f(n)
        return mem[n]
    return memoised_f


# Method 1: does not depend on any library
@memoise
def count_and_say(n):
    """
    38. Count and Say

    The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

    Note: Each term of the sequence of integers will be represented as a string.

    https://leetcode.com/problems/count-and-say/

    """

    if n == 1:
        return '1'
    else:
        count = count_and_say(n-1)
        say = ''
        d, c = count[0], 1
        for i in count[1:]:
            if i == d:
                c += 1
            else:
                say += str(c) + d
                d = i
                c = 1
        say += str(c) + d
        return say


# # Method 2: use itertools.groupby
# from itertools import groupby
#
#
# @memoise
# def count_and_say(n):
#
#     if n == 1:
#         return "1"
#     else:
#         count = count_and_say(n-1)
#         count_split = [''.join(g) for _, g in groupby(count)]
#         say = ''.join([str(len(i))+i[0] for i in count_split])
#         return say


if __name__ == '__main__':
    print(count_and_say(1))
    print(count_and_say(2))
    print(count_and_say(3))
    print(count_and_say(4))
    print(count_and_say(5))
