# NOTE


def reverse_int(x):
    """
    7. Reverse Integer

    Given a 32-bit signed integer, reverse digits of an integer.

    Note: Assume we are dealing with an environment which could only store integers within the 32-bit
    signed integer range: [−2**31,  2**31 − 1]. For the purpose of this problem,
    assume that your function returns 0 when the reversed integer overflows.

    https://leetcode.com/problems/reverse-integer/

    """

    sign = 1 if x >= 0 else -1
    abs = x * sign
    rev = 0

    while abs:
        digit = abs % 10
        rev = rev * 10 + digit
        abs = abs // 10

    rev = rev * sign

    return rev if -2**31 <= rev <= 2**31-1 else 0


if __name__ == '__main__':
    print(reverse_int(123))
    print(reverse_int(-123))
    print(reverse_int(120))
