'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

**Example 1**

`Input: root = [2,1,3], p = 1`
`Output: 2`

Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
'''


class StackSolution:
    def inorderSuccessor(self, root, p):
        arr = []
        self.inorder(root, arr)
        if arr[-1].val == p.val:
            return None
        for i, el in enumerate(arr):
            if el.val == p.val:
                return arr[i+1]
        return None

    def inorder(self, root, arr):
        if not root:
            return
        self.inorder(root.left, arr)
        if root:
            arr.append(root)
        self.inorder(root.right, arr)


class IterativeOptimalSolution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor
