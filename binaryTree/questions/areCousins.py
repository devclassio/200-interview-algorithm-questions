import collections

'''
https://hackmd.io/@YargtAEbS02eDE3upLu27g/BJJAIN1eP#Are-Cousins
Problem

Given a binary tree and two node values, return whether the two nodes are cousins.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

Example:

Given:
     1
   /   \
  2     3
 /
4

n1 = 3, n2 = 4

Return: false

Given:
     1
   /   \
  2     3
 /       \
4         5

n1 = 4, n2 =5

Return: true
'''


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


def areCousinsIterative(root, n1, n2):
    return True


def getLevelsRecursive(root):
    if root is None:
        return []

    def cousinAux(q, res):
        if len(q) == 0:
            return res

        current, i = q.popleft()
        if current is None:
            return res

        if current.left is None and current.right is None:
            return cousinAux(q, res)

        if len(res) - 1 == i:
            res.append([])

        level = res[i + 1]

        if current.left is not None:
            level.append((current.left.data, current.data))
            q.append((current.left, i + 1))

        if current.right is not None:
            level.append((current.right.data, current.data))
            q.append((current.right, i + 1))

        res[i + 1] = level
        return cousinAux(q, res)

    return cousinAux(collections.deque(
        [(root, 0)]), collections.deque([[(root.data, None)]]))


def areCousins(root, n1, n2):
    levels = getLevelsRecursive(root)
    print(list(levels))
    for level in levels:
        lN1 = None
        lN2 = None
        for pair in level:
            child, _parent = pair
            if child == n1:
                lN1 = pair
            if child == n2:
                lN2 = pair
        if lN1 is None or lN2 is None:
            continue
        _l1c, l1p = lN1
        _l2c, l2p = lN2
        if l1p is not l2p:
            return True
    return False


def areCousinsBFS(root, n1, n2):
    if root is None or n1 is None or n2 is None:
        return False
    q = collections.deque([(root, None, 0)])
    n1WithParent = (None, None, None)
    n2WithParent = (None, None, None)
    while len(q) > 0:
        (current, parent, level) = q.popleft()

        if current.data == n1:
            n1WithParent = (n1, parent, level)
            if n2WithParent[0] is not None:
                _val, l2Parent, l2 = n2WithParent
                if l2 == level and parent != l2Parent:
                    return True
                else:
                    return False

        if current.data == n2:
            n2WithParent = (n2, parent, level)
            if n1WithParent[0] is not None:
                _val, l1Parent, l1 = n1WithParent
                if l1 == level and parent != l1Parent:
                    return True
                else:
                    return False

        if current.left is not None:
            q.append((current.left, current, level + 1))
        if current.right is not None:
            q.append((current.right, current, level + 1))

    return False


'''
Problem

Given a binary tree and two node values, return whether the two nodes are cousins.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

Example:

Given:
     1
   /   \
  2     3
 /
4

n1 = 3, n2 = 4

Return: false

Given:
     1
   /   \
  2     3
 /       \
4         5

n1 = 4, n2 =5

Return: true
'''


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
print(areCousins(root, 2, 3))
print(areCousinsBFS(root, 2, 3))
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
print(areCousins(root, 4, 6))
print("\n")

root = Node(1)
print("**** Test 2 **** ")
print(areCousins(root, 3, 4))
print(areCousinsBFS(root, 3, 4))
print("\n")

root = None
print("**** Test 3 **** ")
print(areCousins(root, 4, 4))
print(areCousinsBFS(root, 4, 4))
print("\n")

'''
Input:
          1
        /   \
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
print(areCousins(root, 4, 6))
print(areCousinsBFS(root, 4, 6))
