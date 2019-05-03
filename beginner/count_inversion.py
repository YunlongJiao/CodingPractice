# NOTE:


# # Method 1
#
# def count_inversion(arr):
#     """
#     Count inversion number of a permutation.
#
#     https://www.geeksforgeeks.org/counting-inversions/
#
#     """
#
#     n = len(arr)
#     s = 0
#     for i in range(1, n):
#         for j in range(i):
#             if arr[i] < arr[j]:
#                 s += 1
#
#     return s


# Method 2

def merge_sort(arr, left, middle, right):

    s = 0
    for j in range(middle+1, right+1):
        i = j
        while i > left and arr[i] < arr[i-1]:  # i>=left will cause arr[-1] to call the last element without warning!
            arr[i-1], arr[i] = arr[i], arr[i-1]  # in-place change to mutable list
            i -= 1
            s += 1

    return s


def count_inversion(arr, l, r):
    """
    Count inversion number of a permutation.

    https://www.geeksforgeeks.org/counting-inversions/

    """

    if l == r:
        return 0
    else:
        mid = (l+r)//2
        s1 = count_inversion(arr, l, mid)
        s2 = count_inversion(arr, mid+1, r)
        c = merge_sort(arr, l, mid, r)
        return s1+s2+c


if __name__ == '__main__':

    arr = [2, 4, 1, 3, 5]

    print(count_inversion(arr, 0, len(arr)-1))
