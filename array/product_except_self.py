# NOTE
# Two-way pass to sandwich the right product!


def product_except_self(nums):
    """
    238. Product of Array Except Self

    Given an array nums of n integers where n > 1,
    return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

    Note: Please solve it without division and in O(n).

    Follow up:
    Could you solve it with constant space complexity?
    (The output array does not count as extra space for the purpose of space complexity analysis.)

    https://leetcode.com/problems/product-of-array-except-self/

    """

    n = len(nums)
    out = [1]*n
    forward_prod = 1
    backward_prod = 1

    for i in range(n-1):
        forward_prod *= nums[i]
        backward_prod *= nums[n-1-i]
        out[i+1] *= forward_prod
        out[n-2-i] *= backward_prod

    return out


if __name__ == '__main__':
    print(product_except_self([1,2,3,4]))
