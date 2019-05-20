# NOTE:
# Memoisation accelerates the computation in recursion!


def memoise(f):
    """
    Memoisation accelerates the computation!

    https://github.com/jcboyd/python-notes/blob/master/main.py

    """

    mem = {}

    def memoised_f(*args):
        key = tuple(args)
        if key not in mem:
            mem[key] = f(*args)
        return mem[key]
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
        y = power_calc(x, n//2)
        if n % 2 == 0:
            return y*y
        else:
            return y*y*x


if __name__ == '__main__':

    x = 5
    n = 9

    print(power_calc(x, n))
