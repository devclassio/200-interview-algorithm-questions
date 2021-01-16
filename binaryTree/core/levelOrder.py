'''
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


class SolutionIterative:
    def levelOrder(self, root):
        if root is None:
            return []

        def bfs(root):
            while len(stack) > 0:
                # current node
                current = stack.pop()
                node, level = current[0], current[1]

                # handle levelling
                if len(levels) - 1 < level:
                    levels.append([node.val])
                else:
                    levels[level].append(node.val)

                # add to stack
                if node is not None:
                    if node.right is not None:
                        stack.append((node.right, level + 1))
                    if node.left is not None:
                        stack.append((node.left, level + 1))
        levels = []
        stack = [(root, 0)]
        bfs(root)
        return levels


class SolutionRecursive:
    def levelOrder(self, root):
        if root is None:
            return []

        def bfs(root):
            if len(stack) == 0:
                return

            # current node
            current = stack.pop()
            node, level = current[0], current[1]

            # handle levelling
            if len(levels) - 1 < level:
                levels.append([node.val])
            else:
                levels[level].append(node.val)

            # add to stack
            if node is not None:
                if node.right is not None:
                    stack.append((node.right, level + 1))
                if node.left is not None:
                    stack.append((node.left, level + 1))

            bfs(root)
        levels = []
        stack = [(root, 0)]
        bfs(root)
        return levels
