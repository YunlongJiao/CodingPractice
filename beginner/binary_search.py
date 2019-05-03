# NOTE:
# Remove mid too in the ignored halves for cases when x does not exist; otherwise dead loop!


def binary_search(arr, l, r, x):
    """
    It returns location of x in given array arr if present, else returns -1.

    https://www.geeksforgeeks.org/binary-search/

    """

    while l <= r:
        mid = int(l + (r-l) / 2)
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            l = mid + 1  # ignore left half plus mid
        elif x < arr[mid]:
            r = mid - 1  # ignore right half plus mid
        else:
            raise ValueError('Should not occur unless wrong implementation!')

    return -1


if __name__ == '__main__':

    arr = [2, 3, 4, 10, 40]
    x = 5

    ind = binary_search(arr, 0, len(arr)-1, x)
    print(ind)
