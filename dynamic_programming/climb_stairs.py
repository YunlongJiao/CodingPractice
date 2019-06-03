# NOTE


def memoise(f):
    mem = {}

    def memoised_f(x):
        if x not in mem:
            mem[x] = f(x)
        return mem[x]
    return memoised_f


@memoise
def climb_stairs(n):
    """
    70. Climbing Stairs

    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    Note: Given n will be a positive integer.

    https://leetcode.com/problems/climbing-stairs/

    """

    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return climb_stairs(n-1) + climb_stairs(n-2)


if __name__ == '__main__':
    print(climb_stairs(2))
    print(climb_stairs(3))
