# NOTE
# First solution is recursive while second solution is iterative!


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self):
        p = self
        while p is not None:
            print(p.val)
            p = p.next


# # Method 1: Recursive O(n) time and O(n) space (implicit stack space due to recursion)
# # This solution was Java from https://leetcode.com/problems/reverse-linked-list/solution/
# def reverse_list(head):
#
#     if head is None or head.next is None:
#         return head
#     else:
#         p = reverse_list(head.next)
#         head.next.next = head
#         head.next = None
#         return p


# Method 2: Recursive O(n) time and O(1) space
def reverse_list(head):
    """
    206. Reverse Linked List

    Reverse a singly linked list.

    https://leetcode.com/problems/reverse-linked-list/

    """

    prev, curr = None, head

    while curr is not None:
        next_tmp = curr.next
        curr.next = prev
        prev = curr
        curr = next_tmp

    return prev


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    l = reverse_list(head)
    l.print_list()
