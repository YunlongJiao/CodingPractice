# NOTE
# While the following implementation uses Counter but needs to sort the keys and hash into a dict,
# since the alphabet is fixed (a-z), one could simple categorizes the occurrence of each letter, see Approach 2 of
# https://leetcode.com/problems/group-anagrams/solution/


from collections import Counter


def group_anagrams(strs):
    """
    49. Group Anagrams

    Given an array of strings, group anagrams together.
    Note:
    - All inputs will be in lowercase.
    - The order of your output does not matter.

    https://leetcode.com/problems/group-anagrams/

    """

    counts = dict()
    anagrams = []

    for s in strs:
        cs = Counter(s)
        cs = ''.join([i + str(cs[i]) for i in sorted(cs)])
        if cs in counts:
            anagrams[counts[cs]].append(s)
        else:
            counts[cs] = len(anagrams)
            anagrams.append([s])

    return anagrams


if __name__ == '__main__':
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
