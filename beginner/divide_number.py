# NOTE:
# Dynamic programming solution should be equiv to recursion with memoisation !(?)


def memoise(f):
    mem = {}

    def memoised_f(n, k, min_val):
        key = tuple([n, k, min_val])
        if key not in mem:
            mem[key] = f(n, k, min_val)
        return mem[key]
    return memoised_f


@memoise
def divide_number(n, k, min_val):
    """
    Given a positive integer n,
    find number of ways to divide n in four parts or represent n as sum of four positive integers.
    Here n varies from 0 to 5000.

    https://www.geeksforgeeks.org/count-number-of-ways-to-divide-a-number-in-4-parts/

    """

    if k < 1 or n < min_val*k:
        return 0
    elif k == 1 and n >= min_val*k:
        return 1
    else:
        return sum([divide_number(n-i, k-1, i) for i in range(min_val, n//2+1)])


if __name__ == '__main__':

    n = 8
    print(divide_number(n, 4, 1))
