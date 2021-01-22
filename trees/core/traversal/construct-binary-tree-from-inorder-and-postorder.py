'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

     3
    / \
    9 20
      / \
     15  7
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ImprovedRecursiveSolution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)

        '''
        Why does swapping order of root.right and root.left break code?
        That's because inorder traversal goes 'Left-Parent-Right' and 
        postorder traversal goes 'Left-Right-Parent'. 
        And, postorder.pop() keeps picking the right-most element of the list, 
        that means it should go 'Parent-(one of parents of) Right (subtree) - Left'. 
        So, switching the order doesn't work.

        inorder: [1,2,3]
        postorder: [1,3,2]
        '''

        root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)

        return root
