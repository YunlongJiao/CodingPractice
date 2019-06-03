# NOTE
# Typical question involving two pointers moving inward!


def container_most_water(height):
    """
    11. Container With Most Water

    Given n non-negative integers a1, a2, ..., an ,
    where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
    Find two lines, which together with x-axis forms a container,
    such that the container contains the most water.

    https://leetcode.com/problems/maximum-subarray/

    Solution is taken from
    https://leetcode.com/problems/container-with-most-water/discuss/6091/Easy-Concise-Java-O(N)-Solution-with-Proof-and-Explanation

    """

    max_area = 0

    begin, end = 0, len(height)-1

    while begin < end:
        max_area = max(max_area, (end - begin) * min(height[begin], height[end]))
        if height[begin] < height[end]:  # if begin and end have same height, does not matter which to move inward
            begin += 1
        else:
            end -= 1

    return max_area


if __name__ == '__main__':
    print(container_most_water([1,8,6,2,5,4,8,3,7]))
    print(container_most_water([1,8,6,2,5,4,8,3,7]))
