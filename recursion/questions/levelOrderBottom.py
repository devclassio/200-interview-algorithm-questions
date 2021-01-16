'''
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/solution/
Approach 1: Recursion: DFS Preorder Traversal
Intuition

The first step is to ensure that the tree is not empty. The second step is to implement the recursive function helper(node, level), which takes the current node and its level as the arguments.

Algorithm for the Recursive Function

Here is its implementation:

Initialize the output list levels. The length of this list determines which level is currently updated. You should compare this level len(levels) with a node level level, to ensure that you add the node on the correct level. If you're still on the previous level - add the new level by adding a new list into levels.

Append the node value to the last level in levels.

Process recursively child nodes if they are not None: helper(node.left / node.right, level + 1).
'''


class SolutionDFSLeetCode:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels[::-1]


class SolutionOmer:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        def bfs(root):
            if len(stack) == 0:
                return

            # current
            current = stack.pop()
            node, level = current[0], current[1]

            # levelling
            if len(levels) - 1 < level:
                levels.append([node.val])
            else:
                levels[level].append(node.val)

            # queue
            if node is not None:
                if node.right is not None:
                    stack.append((node.right, level + 1))
                if node.left is not None:
                    stack.append((node.left, level + 1))

            bfs(root)
        levels = []
        stack = [(root, 0)]
        bfs(root)
        levels.reverse()
        return levels
