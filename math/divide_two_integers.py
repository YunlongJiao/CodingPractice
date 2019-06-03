# NOTE
# While both solutions are O(log m),
# first solution is top-down but it is technically not valid due to the use of mod operation,
# second solution is bottom-up and conform to the requirements!


# # Method 1:
# def memoise(f):
#     mem = {}
#     def memoised_f(*args):
#         key = tuple(args)
#         if key not in mem:
#             mem[key] = f(*args)
#         return mem[key]
#     return memoised_f
#
#
# @memoise
# def divide_two_integers_util(m, n):
#     # m >= 0, n > 0
#
#     if m < n:
#         return 0, m  # quotient, remainder
#     else:
#         q, r = divide_two_integers_util(m//2, n)
#         r0 = m - (m//2) - (m//2)
#         q1, r1 = (1, r + r + r0 - n) if r + r + r0 >= n else (0, r + r + r0)
#         return q + q + q1, r1


# Method 2:
def divide_two_integers_util(m, n):
    # m >= 0, n > 0

    q, d, r = 1, n, m
    ans = 0
    while r >= d:
        r -= d
        d += d  # divisor grows exponentially
        ans += q
        q += q
        if r < d:
            # reset divisor after its exponential growth exceeds remainder
            d = n
            q = 1

    return ans, r


def divide_two_integers(dividend, divisor):
    """
    29. Divide Two Integers

    Given two integers dividend and divisor,
    divide two integers without using multiplication, division and mod operator.
    Return the quotient after dividing dividend by divisor.
    The integer division should truncate toward zero.

    https://leetcode.com/problems/divide-two-integers/

    The second solution above is an equiv to one taken from
    https://leetcode.com/problems/divide-two-integers/discuss/13402/Fast-and-simple-Python-solutions-(56ms-64ms).-No-Bitwise-Operators.

    """

    sign = (dividend >= 0 and divisor > 0) or (dividend <= 0 and divisor < 0)
    dividend = -dividend if dividend < 0 else dividend
    divisor = -divisor if divisor < 0 else divisor

    quotient, _ = divide_two_integers_util(dividend, divisor)

    return min(quotient, 2147483647) if sign else max(-quotient, -2147483648)


if __name__ == '__main__':
    print(divide_two_integers(10, 3))
    print(divide_two_integers(7, -3))
