# NOTE
# The first solution is O(n**2) time with O(n) space, while the second is O(n log n) time with O(n) space!
# The problem is practically to implement pandas.Series(arr).rank(method='dense').reindex_like(arr),
# see https://www.geeksforgeeks.org/rank-elements-array/ for pandas.Series(arr).rank(method='average').reindex_like(arr)


# def reassign_priorities(arr):
#
#     n = len(arr)
#     aux = list(range(1,n+1))
#     return [aux[arr.index(i)] for i in arr]


def reassign_priorities(arr):
    """
    Given an array of task priorities represented by integers ranging from 1 to 99, reassign priorities such that:
    after reassignment, relative ordering of two tasks with different priorities are maintained,
    tasks sharing same priorities will still have the same priorities,
    the top priority is reassigned to 1 and incremental between adjacent priorities is by 1.

    For example, given a list of task priorities [1,3,7,3], the expected reassignment is [1,2,3,2].

    This question was taken from Rafa's coding interview.

    """

    n = len(arr)
    arr_sorted = sorted(arr)
    arr_dict = dict()

    val, rank = arr_sorted[0], 1
    for i in range(n):
        if arr_sorted[i] != val:
            rank += 1
        if arr_sorted[i] not in arr_dict:
            arr_dict[arr_sorted[i]] = rank
        val = arr_sorted[i]

    return [arr_dict[i] for i in arr]


if __name__ == '__main__':

    prioritiesList = [1,3,7,3]
    print(reassign_priorities(prioritiesList))
