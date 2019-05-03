# NOTE:
# Two ways - Use sum formula or use XOR..(?)


def find_missing(arr):
    """
    You are given a list of n-1 integers and these integers are in the range of 1 to n.
    There are no duplicates in list. One of the integers is missing in the list.
    Write an efficient code to find the missing integer.

    https://www.geeksforgeeks.org/find-the-missing-number/

    """

    s = sum(arr)
    n = len(arr) + 1
    miss = n*(n+1)/2 - s

    return int(miss)


if __name__ == '__main__':

    arr = [1, 2, 4, 6, 3, 7, 8]

    n = find_missing(arr)
    print(n)
