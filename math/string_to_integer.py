# NOTE
# While first solution is more concise but uses regex, second does not utilize any additional library!


# import re
#
#
# def string_to_integer(str):
#
#     p = re.compile('^ *[-|+]?\d+')
#     found = p.findall(str)
#     if len(found) == 0:
#         return 0
#     elif len(found) == 1:
#         num = int(found[0].lstrip())
#         return num if -2147483648 <= num <= 2147483647 else -2147483648 if num < 0 else 2147483647
#     else:
#         raise ValueError


def string_to_integer(str):
    """
    8. String to Integer (atoi)

    Implement atoi which converts a string to an integer.
    The function first discards as many whitespace characters as necessary,
    until the first non-whitespace character is found. Then, starting from this character,
    takes an optional initial plus or minus sign followed by as many numerical digits as possible,
    and interprets them as a numerical value.

    The string can contain additional characters after those that form the integral number,
    which are ignored and have no effect on the behavior of this function.

    If the first sequence of non-whitespace characters in str is not a valid integral number,
    or if no such sequence exists because either str is empty or it contains only whitespace characters,
    no conversion is performed.

    If no valid conversion could be performed, a zero value is returned.

    Note:
    Only the space character ' ' is considered as whitespace character. Assume we are dealing with an environment
    which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
    If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

    https://leetcode.com/problems/string-to-integer-atoi/

    """

    i = 0
    n = len(str)
    while i < n and str[i] == ' ':
        i += 1

    num, sign = 0, 1
    if i < n and str[i] == '-':
        sign = -1
        i += 1
    elif i < n and str[i] == '+':
        i += 1

    numbers = {'0','1','2','3','4','5','6','7','8','9'}
    while i < n and str[i] in numbers:
        num = num * 10 + int(str[i])
        i += 1

    return num * sign if -2147483648 <= num * sign <= 2147483647 else -2147483648 if sign == -1 else 2147483647


if __name__ == '__main__':
    print(string_to_integer("42"))
    print(string_to_integer("   -42"))
    print(string_to_integer("4193 with words"))
    print(string_to_integer("words and 987"))
    print(string_to_integer("-91283472332"))
