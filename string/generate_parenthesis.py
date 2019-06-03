# NOTE
# First solution is inefficient brute-force recursion, while the second is backtracking based in O(4**n/sqrt(n)) time!
# See a similar topic of checking parentheses at ./valid_parentheses.py


def memoise(f):
    mem = {}
    def memoised_f(n):
        if n not in mem:
            mem[n] = f(n)
        return mem[n]
    return memoised_f


# # Method 1:
# @memoise
# def generate_parenthesis_util(n):
#     # returns set instead of list
#     if n == 0:
#         return {''}
#     else:
#         combns = generate_parenthesis_util(n-1)
#         n_positions = 2 * (n - 1) + 1
#         res = set()
#         for combn in combns:
#             for i in range(n_positions):
#                 for j in range(i, n_positions):
#                     new_combn = combn[:i] + '(' + combn[i:j] + ')' + combn[j:]
#                     res.add(new_combn)
#         return res
#
#
# def generate_parenthesis(n):
#
#     return list(generate_parenthesis_util(n))


# Method 2:
@memoise
def generate_parenthesis(n):
    """
    22. Generate Parentheses

    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    https://leetcode.com/problems/generate-parentheses/

    This backtracking based solution was taken from
    https://leetcode.com/problems/generate-parentheses/solution/

    """

    if n == 0:
        return ['']
    else:
        res = []
        for c in range(n):
            for left in generate_parenthesis(c):
                for right in generate_parenthesis(n-1-c):
                    res.append('({}){}'.format(left, right))
        return res


if __name__ == '__main__':
    print(generate_parenthesis(3))
