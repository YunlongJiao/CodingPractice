# NOTE:
# OOP implementation of a tree/root!
# Cannot write isBST as a method as self.node would not update recursively!(?)


class Node:

    def __init__(self, data):
        """
        A program to check if a binary tree is BST or not.

        https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

        """

        self.data = data
        self.left = None
        self.right = None


def is_BST_util(node, mini, maxi):

    if node is None:
        return True
    elif node.data < mini or node.data > maxi:
        return False
    else:
        return is_BST_util(node.left, mini, node.data-1) and \
               is_BST_util(node.right, node.data+1, maxi)  # cannot be defined within class (?)


def is_BST(node):

    return is_BST_util(node, -float('inf'), float('inf'))


if __name__ == '__main__':

    root1 = Node(3)
    root1.left = Node(2)
    root1.right = Node(5)
    root1.left.left = Node(1)
    root1.left.right = Node(4)

    print(is_BST(root1))

    root2 = Node(4)
    root2.left = Node(2)
    root2.right = Node(5)
    root2.left.left = Node(1)
    root2.left.right = Node(3)

    print(is_BST(root2))
