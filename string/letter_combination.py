# NOTE
# See a similar topic of generating permutations at ../beginner/permute_string.py


def letter_combination(digits):
    """
    17. Letter Combinations of a Phone Number

    Given a string containing digits from 2-9 inclusive,
    return all possible letter combinations that the number could represent.
    A mapping of digit to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letters.

    https://leetcode.com/problems/letter-combinations-of-a-phone-number/

    """

    if len(digits) == 0:
        return []
    else:
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        combinations = ['']
        for digit in reversed(digits):
            tmp = []
            for letter in digit_to_letters[digit]:
                tmp += [letter+i for i in combinations]
            combinations = tmp

        return combinations


if __name__ == '__main__':
    print(letter_combination("23"))
