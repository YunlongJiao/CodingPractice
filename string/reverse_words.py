# NOTE


def reverse_words(s):
    """
    151. Reverse Words in a String
    Given an input string, reverse the string word by word.

    https://leetcode.com/problems/reverse-words-in-a-string/

    """

    return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    print(reverse_words("the sky is blue"))
    print(reverse_words("  hello world!  "))
    print(reverse_words("a good   example"))
