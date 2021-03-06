'''

DFS stands for depth first search. So in this tree traversal method we go as deep as possible, hit a leaf and then continue to explore the rest of the neighbors.

Let's look at the following tree as an example:

```
        1
      /   \
    2       3
   /         \
 4            5
```

**Traversal Example**

Like mentioned above a valid DFS traversal could visit the nodes in the graph in the following order:

`1->2->4->3->5`

Another valid DFS traversal could be:

`1->3->5->2->4`

Let's look at an iterative and recursive DFS implmentation.
'''


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def visitNode(node):
    if node:
        print(node.val)


def iterativeDfs(root):
    if not root:
        return
    q = [root]
    while q:
        current = q.pop(0)
        if not current:
            return
        visitNode(current)
        if current.left:
            q.append(current.left)
            continue
        if current.right:
            q.append(current.right)


def recursiveDfs(root):
    if not root:
        return

    def helper(q):
        if not q:
            return
        current = q.pop(0)
        if not current:
            return
        visitNode(current)
        if current.left:
            q.append(current.left)
            helper(q)
        if current.right:
            q.append(current.right)
            helper(q)
    q = [root]
    helper(q)
