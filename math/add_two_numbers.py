# NOTE
# Remember to make sure remainder is not zero before exiting the loop!


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self):
        l = self
        while l is not None:
            print(l.val)
            l = l.next


def add_two_numbers(l1, l2):
    """
    2. Add Two Numbers

    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    https://leetcode.com/problems/add-two-numbers/

    """

    p1, p2 = l1, l2
    # Case 1: output a linked list
    head, r = ListNode(0), 0
    l = head
    # # Case 2: output an integer
    # s, r, b = 0, 0, 1

    while p1 is not None or p2 is not None or r != 0:  # make sure nothing is left in the remainder as well
        d1 = p1.val if p1 is not None else 0
        d2 = p2.val if p2 is not None else 0
        d = (d1 + d2 + r) % 10
        r = (d1 + d2 + r) // 10
        # Case 1: output a linked list
        l.next = ListNode(d)
        l = l.next
        # # Case 2: output an integer
        # s += b * d
        # b *= 10
        p1 = p1.next if p1 is not None else p1
        p2 = p2.next if p2 is not None else p2

    # Case 1: output a linked list
    return head.next
    # # Case 2: output an integer
    # return s


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l = add_two_numbers(l1, l2)

    # Case 1: output a linked list
    l.print_list()
    # # Case 2: output an integer
    # print(l)
