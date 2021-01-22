'''
REVIEW!!! Note: All nodes of the subtreeees!

Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

 

Example 1:


Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6
 

Constraints:

The numbrt of the node in the tree will be in the range [0, 1000].
-1000 <= Node.val <= 1000
'''


class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0

        def helper(root):
            if root is None:
                return True

            l, r = helper(root.left), helper(root.right)

            if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
                self.count += 1
                return True

            return False

        helper(root)
        return self.count
