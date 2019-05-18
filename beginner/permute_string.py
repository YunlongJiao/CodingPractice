# NOTE


def permute_string(s):
    """
    Write a program to print all permutations of a given string

    https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

    """

    if len(s) == 1:
        return [s]
    else:
        c = s[0]
        l = []
        for i in permute_string(s[1:]):
            for pos in range(len(s)):
                l.append(i[:pos]+c+i[pos:])
        return l


if __name__ == '__main__':
    print(permute_string("ABC"))
