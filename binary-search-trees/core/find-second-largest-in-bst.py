'''
Let's write an algorithm to find the largest node in a binary search tree!
'''


class Solution:
    def findLargest(self, root):
        current = root
        while current and current.right:
            current = current.right
        return current

    def findSecondLargest(self, root):
        if not root or (not root.left and not root.right):
            '''
            We need atleast 2 nodes!
            '''
            return root

        # right most node that has left subtree
        if root.left and not root.right:
            return self.findSecondLargest(root.left)

        # were at parent of largest
        if (root.right and
                not root.right.left and
                not root.right.right):
            return root

        return self.findSecondLargest(root.right)
