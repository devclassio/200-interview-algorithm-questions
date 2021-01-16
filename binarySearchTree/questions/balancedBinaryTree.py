
class Solution:

    def getHeight(self, root):
        if root is None:
            return 0

        lh = self.getHeight(root.left) + 1
        rh = self.getHeight(root.right) + 1

        return max(lh, rh)

    def isBalanced(self, root):
        if root is None:
            return True

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        return abs(leftHeight - rightHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


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
