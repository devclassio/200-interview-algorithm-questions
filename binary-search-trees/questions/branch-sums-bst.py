import collections


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def dfs(root, sums=[]):
    if root is None:
        return sums
    q = collections.deque([(root, root.data)])
    while len(q) > 0:
        current, cs = q.popleft()
        if current.left:
            q.append((current.left, cs + current.left.data))
        if current.right:
            q.append((current.right, cs + current.right.data))

        if current.right is None and current.left is None:
            sums.append(cs)
    return sums


def dfsRecursive(root):
    if root is None:
        return []
    branches = collections.deque([])

    def dfsHelper(root, currentSum, branches):
        currentSum = currentSum + root.data
        if isLeaf(root):
            return branches.append(currentSum)
        dfsHelper(root.left, currentSum, branches)
        dfsHelper(root.right, currentSum, branches)
    dfsHelper(root, 0, branches)
    return branches


def isLeaf(node):
    return node.left is None and node.right is None


'''
Input:
      1
    /   \
   2     3
 
 Output:
 [3, 4]
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print("Test 0...")
print(list(dfs(root, collections.deque([]))))
print(list(dfsRecursive(root)))

'''
Input:
      1
    /   \
   2     3
 4  5   6  7
 Output:
 [7,8,10,11]
 '''

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

print("Test 1...")
print(list(dfs(root, collections.deque([]))))
print(list(dfsRecursive(root)))

root = Node(1)
print("Test 2...")
print(list(dfs(root, collections.deque([]))))
print(list(dfsRecursive(root)))

root = None
print("Test 3...")
print(list(dfs(root, collections.deque([]))))
print(list(dfsRecursive(root)))
