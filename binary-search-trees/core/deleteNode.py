'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

**Example 1**

`Input: root = [5,3,6,2,4,null,7], key = 3`

`Output: [5,4,6,2,null,null,7]`
'''


class Solution:
    def successor(self, node):
        current = node.right
        while current.right:
            current = current.right
        return current

    def predecessor(self, node):
        current = node.left
        while current.left:
            current = current.left
        return current

    def deleteNode(self, root, key):
        if not root:
            return root
        if root.val == key:
            if not root.left and not root.right:  # no children
                root = None
            elif root.right:
                root = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        elif root.val > key:
            root.right = self.deleteNode(root.left, key)
        else:
            root.left = self.deleteNode(root.right, key)
        return root
