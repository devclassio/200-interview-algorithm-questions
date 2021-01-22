'''
BFS is a tree traversal method. We search the graph level by level.

- The concept is a layered traversal.
- This means we start at the root of the node and we begin a "levelled" traversal.

Let's define the **level or depth of a given node the amount of edges between that node and the root**.

Let's look at the following tree as an example:

```
        1
      /   \
    2       3
   /         \
 4            5
```

**Level 0**

All nodes at distance 0 from root. `{1}`

**Level 1**

All nodes at distance 1 from root. `{2, 3}`

**Level 2**

All nodes at distance 2 from root. `{4, 5}`

**Traversal Example**

Like mentioned above a valid BFS traversal could visit the nodes in the graph in the following order:

`1->2->3->4->5`

Another valid BFS traversal could be:

`1->3->2->5->4`

Let's look at an iterative and recursive BFS implmentation.
'''


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def visitNode(node):
    if node:
        print(node.val)


def bfsIterative(root):
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
        if current.right:
            q.append(current.right)


def recursiveBfs(root):
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
        if current.right:
            q.append(current.right)
        helper(q)
    q = [root]
    helper(q)
