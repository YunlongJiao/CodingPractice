# NOTE:
# Python provides min-heap implementation; for max-heap, build a min-heap over negative-arr!
# call heapify on arr[:k] will return None! Make a copy or push one by one
# call res.sort() for heap res will return None! Make a copy or use sorted(res)

import heapq


def k_largest(arr, k):
    """
    Write an efficient program for printing k largest elements in an array.
    Elements in array can be in any order.

    https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/

    """

    assert len(arr) >= k

    res = []
    for i in range(k):
        heapq.heappush(res, arr[i])  # or make a copy first

    for i in range(k, len(arr)):
        # heapq.heappushpop(res, arr[i])
        # # OR
        if arr[i] > res[0]:
            heapq.heapreplace(res, arr[i])

    res = sorted(res, reverse=True)  # or make a copy first

    return res


if __name__ == '__main__':

    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3

    num = k_largest(arr, k)
    print(num)
