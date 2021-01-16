class OptimalSolution:

    def inorderSuccessor(self, root, p):

        candidate = None
        curr = root

        while curr:

            if curr.val == p.val:
                candidate = curr
                curr = None
            elif curr.val > p.val:
                candidate = curr
                curr = curr.left
            else:
                curr = curr.right

        return candidate
