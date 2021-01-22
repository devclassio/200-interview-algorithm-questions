'''
Inorder traversals are super useful! In a binary search tree an inorder traversal let's us visit all the nodes... well in order :)
In other words, we can visit all nodes in ascending order. This is great as now we understand the direct relation between a binary search tree and a sorted array!.
'''


def visitNode(node):
    print(node.val)


def inorderRecursively(root):
    if root is None:
        return

    def inorderHelper(root):
        inorderHelper(root.left)
        visitNode(root)
        inorderHelper(root.right)

    inorderRecursively(root)
