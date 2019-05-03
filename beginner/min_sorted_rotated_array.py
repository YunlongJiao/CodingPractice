# NOTE
# Duplicates cannot be handled within O(log n) time at all so the following implementation does not accommodate!


def min_sorted_rotated_array(arr, l, r):
    """
    Python program to find minimum element in a sorted and rotated array.

    https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/

    """

    while l <= r:
        if arr[l] <= arr[r]:
            return arr[l]
        else:
            mid = int(l + (r-l)/2)
            if arr[mid] >= arr[l]:
                l = mid + 1
            else:
                r = mid

    return -1


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 1]
    m = min_sorted_rotated_array(arr, 0, len(arr)-1)
    print(m)
