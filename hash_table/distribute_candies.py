# NOTE


def distribute_candies(candies):
    """
    575. Distribute Candies

    Given an integer array with even length, where different numbers in this array represent different kinds of candies.
    Each number means one candy of the corresponding kind.
    You need to distribute these candies equally in number to brother and sister.
    Return the maximum number of kinds of candies the sister could gain.

    https://leetcode.com/problems/distribute-candies/

    """

    return min(len(set(candies)), len(candies)//2)


if __name__ == '__main__':
    print(distribute_candies([1,1,2,2,3,3]))
