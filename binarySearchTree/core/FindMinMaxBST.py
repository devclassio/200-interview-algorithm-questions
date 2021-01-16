'''
Binary Search Tree -> Finding min / max in a binary search tree

As we discussed previously a binary search tree is a recursive data structure.

In any binary search tree we know that the smaller value is the left child, and the larger one is the right child.

Therefore, given a valid BST we know that the smallest and largest nodes will be the leftmost and right most nodes in the tree.
'''


def findMinRecursive(root):
    if root is None or root.left is None:
        return root
    return findMinRecursive(root.left)


def findMinIterative(root):
    current = root
    while current is not None and current.next is not None:
        current = current.left
    return current


def findMaxRecursive(root):
    if root is None or root.right is None:
        return root
    return findMaxRecursive(root.right)


def findMaxIterative(root):
    current = root
    while current is not None and current.next is not None:
        current = current.right
    return current
