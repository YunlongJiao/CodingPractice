# NOTE
# Creating extra node for head, as well as p/p1/p2, is essential in simplifying the logic of the entire code!
# Recursive solution is found at https://leetcode.com/problems/merge-two-sorted-lists/discuss/9771/Simple-5-lines-Python


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self):
        p = self
        while p is not None:
            print(p.val)
            p = p.next


def merge_two_lists(l1, l2):
    """
    21. Merge Two Sorted Lists

    Merge two sorted linked lists and return it as a new list.
    The new list should be made by splicing together the nodes of the first two lists.

    https://leetcode.com/problems/merge-two-sorted-lists/

    """

    p1, p2 = l1, l2
    head = ListNode(0)
    p = head

    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next

    p.next = p1 or p2
    # # or equiv
    # if p1 is None:
    #     p.next = p2
    # if p2 is None:
    #     p.next = p1

    return head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l = merge_two_lists(l1, l2)
    l.print_list()
