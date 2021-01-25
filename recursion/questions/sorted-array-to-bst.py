'''
Full write up at https://devclass.io/sorted-array-to-bst

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

![Uno reverse](../images/tug-tree.gif)

This ^^^ is what building a binary tree from a sorted array would look like in real life... I think ?!

**Example 1**

`Input: [-10,-3,0,5,9]`

`Output:`

      0
     / \
   -3   5
   /     \
 -10      9

'''


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        arrLen = len(nums)
        if arrLen == 0:
            return
        if arrLen == 1:
            return TreeNode(nums[0], None, None)
        if arrLen == 2:
            if nums[0] <= nums[1]:
                leftChild = TreeNode(nums[0], None, None)
                return TreeNode(nums[1], leftChild, None)
            else:
                rightChild = TreeNode(nums[0], None, None)
                return TreeNode(nums[1], None, rightChild)
        m = int(arrLen / 2)
        l = self.sortedArrayToBST(nums[0:m])
        r = self.sortedArrayToBST(nums[m + 1:])
        return TreeNode(nums[m], l, r)
