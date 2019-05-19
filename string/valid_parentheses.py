# NOTE


def valid_parentheses(s):
    """
    20. Valid Parentheses
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

    https://leetcode.com/problems/valid-parentheses/

    """

    is_valid = True
    pairs = {'(':')', '[':']', '{':'}'}

    collect = []
    for c in s:
        if c in pairs:
            collect.append(pairs[c])
        else:
            if len(collect) == 0 or not collect.pop() == c:
                is_valid = False

    if not len(collect) == 0:
        is_valid = False

    return is_valid


if __name__ == '__main__':
    print(valid_parentheses("()[]{}"))
    print(valid_parentheses(""))
    print(valid_parentheses("{[]}"))
    print(valid_parentheses("([)]"))
    print(valid_parentheses("("))
