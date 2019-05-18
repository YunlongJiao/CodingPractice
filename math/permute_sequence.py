# NOTE
# An equiv but much simpler (7-line) implementation is found at
# https://leetcode.com/problems/permutation-sequence/discuss/22607/7-line-Python-solution-get-each-index-by-curr_k-(n-1)!-curr_k-(n-2)!-...-curr_k-0!


def permute_sequence(n, k):
    """
    60. Permutation Sequence
    The set [1,2,3,...,n] contains a total of n! unique permutations.
    By listing and labeling all of the permutations in increasing order.
    Given n and k, return the kth permutation sequence.

    https://leetcode.com/problems/permutation-sequence/

    """

    fac = 1
    for i in range(1, n+1):  # equiv to: fac = math.factorial(n)
        fac *= i

    num = 0
    occurred = set()
    for i in range(n):
        fac /= (n-i)
        idx = n - i
        while idx*fac >= k:
            idx -= 1
        k -= idx*fac  # equiv to: idx, k = divmod(k, fac)

        t = 0
        digit = 0
        for digit in range(n+1):
            if digit not in occurred:
                t += 1
            if t > idx + 1:
                break
        num = num * 10 + digit
        occurred.add(digit)  # in fact, n cannot exceed 9, so may maintain ['1',...,'9'][:n] and remove digit one-by-one

        if k == 0:
            break
        elif k < 0:
            raise ValueError

    return str(num)


if __name__ == '__main__':
    print(permute_sequence(3, 3))
    print(permute_sequence(4, 9))
