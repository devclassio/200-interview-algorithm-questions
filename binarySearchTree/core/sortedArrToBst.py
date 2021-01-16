import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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


'''
Given a sorted array with unique ints, write algo to
create binary search tree with min height

[1,2,3,4,5,6,7], len 7, middle 3
      4
    2   6
   1 3 5 7

[1,2], len 1, middle 0
    1
     2

[1,2,3], len 2, middle 1
     1
    2 3

[1,2,3,4], len 3, middle 1
     1
    2 3
   4
'''


# print(arrToBst([]))
# print(arrToBst([1]))
# print(arrToBst([1, 2]))
# print(arrToBst([1, 2, 3]))
# print(arrToBst([1, 2, 3, 4]))
# print(arrToBst([1, 2, 3, 4, 5]))

print("******* In order 1 *******")
# postOrder(root, [])
# preOrder(root, [])
# inOrder(root, [])
