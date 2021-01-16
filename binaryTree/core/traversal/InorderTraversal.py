'''
Binary Search Tree -> Inorder traversal

The benefit of a BST is the organization of the data in a sorted manner.

With a root node in hand, one of the more common operations we'd like to do is traverse the tree in its sorted order (hence, the name inorder traversal ;) .

Since BSTs are linked Data structures and not continuous we need to write a traversal algo specific to what we know about the tree structure.

Tree traversals are easily done with recursion, so let's write out a recursive inorder traversal.
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
