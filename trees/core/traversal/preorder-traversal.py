class Solution:
    def visitNode(self, node):
        if node:
            print(node.val)

    def postorder(self, root):
        self.postorder(root.left)
        self.visitNode(root)
        self.postorder(root.right)
