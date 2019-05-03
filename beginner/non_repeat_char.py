# NOTE:
# Alternatively keep track of both index and count as https://www.geeksforgeeks.org/kth-non-repeating-character/


def non_repeat_char(string):
    """
    Given a string, find the first non-repeating character in it.

    https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/

    """

    count = {}

    for i, s in enumerate(string):
        if s not in count:
            count[s] = 1
        else:
            count[s] += 1

    for s,c in count.items():
        if c == 1:
            return s

    return -1


if __name__ == '__main__':

    string = 'GeeksforGeeks'

    print(non_repeat_char(string))
