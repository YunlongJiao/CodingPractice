# NOTE


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self):
        p = self
        while p is not None:
            print(p.val)
            p = p.next


def remove_nth_from_end(head, n):
    """
    19. Remove Nth Node From End of List

    Given a linked list, remove the n-th node from the end of list and return its head.
    Note: Given n will always be valid.
    Follow up: Could you do this in one pass?

    https://leetcode.com/problems/remove-nth-node-from-end-of-list/

    """

    pseudo_head = ListNode(-1)
    pseudo_head.next = head
    curr, prev = head, pseudo_head
    n_visited = 0

    while curr is not None:
        curr = curr.next
        n_visited += 1
        if n_visited > n:
            prev = prev.next

    prev.next = prev.next.next

    return pseudo_head.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2

    l = remove_nth_from_end(head, n)
    l.print_list()
