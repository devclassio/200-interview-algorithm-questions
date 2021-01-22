'''
Let's write an algorithm to find the largest node in the tree! Finding the minimum is the exact same (just completely opposite lol) with a few tweaks ;)
'''


class RecursiveSolution:
    def findLargest(self, root):
        if not root or not root.right:
            return root
        return self.findLargest(root.right)

    def findMinRecursive(self, root):
        if root is None or root.left is None:
            return root
        return self.findMinRecursive(root.left)


class IterativeSolution:
    def findLargest(self, root):
        current = root
        while current and current.right:
            current = current.right
        return current
