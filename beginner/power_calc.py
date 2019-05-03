# NOTE:
# Memoisation accelerates the computation in recursion!


def memoise(f):
    """
    Memoisation accelerates the computation!

    https://github.com/jcboyd/python-notes/blob/master/main.py

    """

    mem = {}

    def memoised_f(x, n):
        if n not in mem:
            mem[n] = f(x, n)
        return mem[n]

    return memoised_f


@memoise
def power_calc(x, n):
    """
    Given two integers x and n, write a function to compute x to the power of n.
    We may assume that x and n are small and overflow doesn’t happen.

    https://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/

    """

    if n == 1:
        return x
    else:
        return power_calc(x, n//2) * power_calc(x, n - n//2)


if __name__ == '__main__':

    x = 5
    n = 9

    print(power_calc(x, n))