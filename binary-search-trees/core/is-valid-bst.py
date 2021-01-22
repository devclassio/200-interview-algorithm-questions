'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

**Example 1**

`Input: root = [2,1,3]`

`Output: true`

**Example 2**

`Input: root = [5,1,4,null,null,3,6]`

`Output: false`
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
