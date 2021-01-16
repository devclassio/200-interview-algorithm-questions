'''
Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
Ahh the power of recursion and induction! First of all, let's remember the definition of recursion.
It's simply mathematical induction! 

Now, let's make an observation about a binary search tree. 
Let's assume the tree is `T`
Let's assume the value to insert is `val`

Now, let's frame this problem a bit differently. Say we are searching `T` for a node with value `val`.
Now, since we know that such a node doesn't exist let's add it, exactly where we would have returned `None`
'''


class Solution:
    def insertIntoBST(self, root, val):
        if root is None:
            '''
            Returns Node, so we know that we can invoke this for left/right sub tree!
            '''
            return TreeNode(val, None, None)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root


class SolutionLeftString:
    '''
    This is a hacky solution that basically creates a linked list
    '''

    def setInorder(self, root, sorted):
        if root is None:
            return
        self.setInorder(root.left, sorted)
        sorted.append(root)
        self.setInorder(root.right, sorted)

    def getNewSorted(self, sorted, val):
        # init new node
        newNode = TreeNode(val, None, None)

        # empty tree
        if len(sorted) == 0:
            return [newNode]

        # smallest
        if val < sorted[0].val:
            return [newNode] + sorted

        # largest
        if val > sorted[-1].val:
            return sorted + [newNode]

        # middle
        j = -1
        for i in range(len(sorted)):
            if val > sorted[i-1].val and val <= sorted[i].val:
                print("found insert ", sorted[i-1].val, val, sorted[i].val)
                j = i
                break

        sorted.insert(j, newNode)
        return sorted

    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val, None, None)

        # Sorted list
        sorted = []
        self.setInorder(root, sorted)
        sorted = self.getNewSorted(sorted, val)

        # Create BST
        currentNode = sorted.pop()
        currentNode.left = None
        currentNode.right = None
        root = currentNode
        while len(sorted) > 0:
            currentNode.left = sorted.pop()
            currentNode.right = None
            currentNode = currentNode.left
        currentNode.left = None
        currentNode.right = None

        return root
