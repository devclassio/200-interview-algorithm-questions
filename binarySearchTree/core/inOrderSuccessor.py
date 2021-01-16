'''
CTCI, Page 110, Trees and Graphs

Write an algo to find the "next" node of a given node
in a BST. You may assume that each node has a link to its
parent (?)
'''


class Solution:

    def __init__(self):
        self.candidate = None

    def inorderSuccessor(self, root, p):

        def inOrder(root, parent):

            # Left sub tree
            if root.left is not None:
                inOrder(root.left, root)

            # Root
            if root.val > p.val and self.candidate is None:
                self.candidate = root

            # Right sub tree
            if root.right is not None:
                inOrder(root.right, root)

        inOrder(root, None)
        return self.candidate


'''
This is really important b/c it is basically a binary search on a 
BST with a small variant!

Here we perform a binary search on the BST.

The last value we encounter that is larger than target will
be the right node!

Time Complexity: O(N)
Space Complexity: O(1)
'''


class OptimalSolution:

    def inorderSuccessor(self, root, p):

        candidate = None
        curr = root

        while curr:

            if curr.val > p.val:
                candidate = curr
                curr = curr.left
            else:
                curr = curr.right

        return candidate
