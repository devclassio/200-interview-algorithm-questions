'''
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


class SolutionOptimal:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


class Solution:
    def dfs(self, q, currentSum, sums):
        if len(q) == 0:
            return

        # current
        current = q.pop()
        if current is None:
            return

        # add to Sum
        currentSum += current.val

        if current.right is None and current.left is None:
            sums.append(currentSum)

        # left
        q.append(current.left)
        self.dfs(q, currentSum, sums)

        # right
        q.append(current.right)
        self.dfs(q, currentSum, sums)

    def hasPathSum(self, root, sum):
        if root is None:
            return False
        sums = []
        self.dfs([root], 0, sums)
        for el in sums:
            if el == sum:
                return True
        return False
