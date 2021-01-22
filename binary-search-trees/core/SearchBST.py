'''
This algo works b/c 
'''


def searchRecursive(root, target):
    if target.val == root.val:
        return root

    return searchRecursive(root.left, target) if target.val < root.val else searchRecursive(root.right, target)


def searchIterate(root, target):
    current = root
    while current is not None:
        if current.val == target.val:
            return current

        if current.val < target.val:
            current = current.right
        else:
            current = current.left

    return None
