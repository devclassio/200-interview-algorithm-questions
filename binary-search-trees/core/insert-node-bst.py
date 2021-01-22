'''
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

**Example 1**

`Input: root = [4,2,7,1,3], val = 5`

`Output: [4,2,7,1,3,5]`

**Example 2**

`Input: root = [40,20,60,10,30,50,70], val = 25`

`Output: [40,20,60,10,30,50,70,null,null,25]`

**Example 3**

`Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5`
`Output: [4,2,7,1,3,5]`
'''


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val, None, None)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root
