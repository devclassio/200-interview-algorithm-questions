class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    '''
    This only works when the constrains are:
    1. p and q are present
    2. all tree nodes are unique!
    '''

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        if not l:
            return r
        if not r:
            return l


class SolutionOmer:
    '''
    Passes 29 cases out of 31, too slow for major case
    '''

    def hasDescendant(self, targetNode, q):
        if not q:
            return False

        current = q.pop()
        if not current:
            return False
        if current.val == targetNode.val:
            return True

        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)

        return self.hasDescendant(targetNode, q)

    def lowestCommonAncestor(self, root, p, q):
        self.lca = None

        def helper(root):
            if not root or not p or not q:
                return

            if self.hasDescendant(p, [root]) and self.hasDescendant(q, [root]):
                self.lca = root

            helper(root.left)
            helper(root.right)

        helper(root)
        return self.lca
