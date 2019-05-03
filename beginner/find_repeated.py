# NOTE:
# Many ways - The following sort-and-traverse in O(n log n) time and O(1) space,
# or use count array in O(n) time and O(n) space,
# or use two equations by sum and product in O(n) time and O(1) space (won't work for large n..)
# or Method 3 of https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/ in O(n) time and O(1) space!


# def find_repeated(arr, n):
#     """
#     You are given an array of n+2 elements.
#     All elements of the array are in range 1 to n.
#     And all elements occur once except two numbers which occur twice.
#     Find the two repeating numbers.
#
#     https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/
#
#     """
#
#     res = []
#     arr.sort()
#     for i in range(len(arr)-1):
#         if arr[i] == arr[i+1]:
#             res.append(arr[i])
#
#     return res

def find_repeated(arr, n):
    """
    You are given an array of n+2 elements.
    All elements of the array are in range 1 to n.
    And all elements occur once except two numbers which occur twice.
    Find the two repeating numbers.

    https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

    """

    res = []
    for i in range(n):
        ai = abs(arr[i])
        if arr[ai] < 0:
            res.append(abs(arr[ai]))
        else:
            arr[ai] = -arr[ai]

    return res


if __name__ == '__main__':

    arr = [4, 2, 4, 5, 2, 3, 1]
    n = 5

    i, j = find_repeated(arr, n)
    print(i, j)
