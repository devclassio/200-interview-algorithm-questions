'''
Given a binary search tree and a node in it, find the in-order predecessor of that node in the BST.

The predecessor of a node p is the node with the largest key smaller than p.val.

**Example 1**
Input: root = [2,1,3], p = 2
Output: 1
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
'''


class RecursiveSolution:
    def inorderPredecessor(self, root, p):
        arr = []
        self.inorder(root, arr)
        if arr[0].val == p.val:
            return None
        for i, el in enumerate(arr):
            if el.val == p.val:
                return arr[i-1]
        return None

    def inorder(self, root, arr):
        if not root:
            return
        self.inorder(root.left, arr)
        if root:
            arr.append(root)
        self.inorder(root.right, arr)


class IterativeSolution:
    def inorderPredecessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        predecessor = None
        while root:
            if root.val < p.val:
                predecessor = root
                root = root.right
            else:
                root = root.left
        return predecessor
