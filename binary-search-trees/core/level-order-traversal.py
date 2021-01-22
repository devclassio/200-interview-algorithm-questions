# Definition for a binary tree node.
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


def dfsIterative(root):
    if root is None:
        return []

    q = collections.deque([(root, 0)])
    res = collections.deque([[root.data]])

    while q:
        current, i = q.popleft()

        if current.left is None and current.right is None:
            continue

        if len(res) - 1 == i:
            res.append([])

        level = res[i + 1]

        if current.left is not None:
            q.append((current.left, i + 1))
            level.append(current.left.data)

        if current.right is not None:
            q.append((current.right, i + 1))
            level.append(current.right.data)

        res[i+1] = level

    return res


def dfsR(root):
    if root is None:
        return []

    def dfsRecursive(q, res):
        if not q:
            return res

        # Get current
        root, i = q.pop(0)

        if root.left is None and root.right is None:
            return dfsRecursive(q, res)

        # Is new level
        if len(res) - 1 == i:
            res.append([])

        # Get current level
        level = res[i + 1]

        # Add to level
        if root.left is not None:
            q.append((root.left, i + 1))
            level.append(root.left.data)
        if root.right is not None:
            q.append((root.right, i + 1))
            level.append(root.right.data)

        return dfsRecursive(q, res)

    return dfsRecursive(collections.deque([(root, 0)]), collections.deque([[root.data]]))


'''
Input:
      1
    /   \
   2     3

 Output:
 [[1], [2,3]]
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print("**** Test 0 **** ")
print(list(dfsR(root)))
print(list(dfsIterative(root)))
print("\n")

'''
Input:
      1
    /   \
   2     3
 4  5   6  7
 Output:
 [[1], [2, 3], [4, 5, 6, 7]]
 '''

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

print("**** Test 1 **** ")
print(list(dfsR(root)))
print(list(dfsIterative(root)))
print("\n")

root = Node(1)
print("**** Test 2 **** ")
print(list(dfsR(root)))
print(list(dfsIterative(root)))
print("\n")

root = None
print("**** Test 3 **** ")
print(list(dfsR(root)))
print(list(dfsIterative(root)))
print("\n")

'''
Input:
          1
        /       \
       2     3
     4  5   6  7
    /
   8
 Output:
 [[1], [2, 3], [4, 5, 6, 7], [8]]
 '''

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)

print("**** Test 4 **** ")
print(list(dfsR(root)))
