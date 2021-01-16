'''
CTCI, page 100, Trees and Graphs

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''


class Solution:
    def isValidBST(self, root):

        def isValidAux(root, lowerBound, higherBound):
            if root is None:
                return True

            if root.val >= higherBound or root.val <= lowerBound:
                return False

            return isValidAux(root.left, lowerBound, root.val) and isValidAux(root.right, root.val, higherBound)

        upperBound = float('inf')
        lowerBound = float('-inf')
        return isValidAux(root, lowerBound, upperBound)


'''
Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
'''


'''
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
