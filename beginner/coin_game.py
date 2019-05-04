# NOTE:
# The following uses recursion - dynamic programming solution with extra memory storage of n*n table exists!


def memoise(f):
    mem = {}

    def memoised_f(x):
        key = tuple(x)
        if key not in mem:
            mem[key] = f(x)
        return mem[key]

    return memoised_f


@memoise
def coin_game(arr):
    """
    Consider a row of n coins of values v1 . . . vn, where n is even.
    We play a game against an opponent by alternating turns.
    In each turn, a player selects either the first or last coin from the row,
    removes it from the row permanently, and receives the value of the coin.
    Determine the maximum possible amount of money we can definitely win if we move first.

    https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/

    """

    assert len(arr) % 2 == 0

    if len(arr) == 2:
        return max(arr)
    else:
        return max(arr[0] + min(coin_game(arr[2:]), coin_game(arr[1:-1])),
                   arr[-1] + min(coin_game(arr[:-2]), coin_game(arr[1:-1])))


if __name__ == '__main__':

    arr1 = [5, 3, 7, 10]
    print(coin_game(arr1))

    arr2 = [8, 15, 3, 7]
    print(coin_game(arr2))

    arr3 = [1, 7, 3, 2, 10, 6]
    print(coin_game(arr3))
