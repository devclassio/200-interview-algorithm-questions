# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        tail, current, stack = head, head, [head]
        while current.next is not None:
            current = current.next
            if current.next is None:
                tail = current
            else:
                stack.append(current)

        head.next = None
        current = tail
        lenStack = len(stack)
        for i in range(lenStack):
            node = stack.pop(lenStack - i - 1)
            current.next = node
            current = node

        return tail

        def reverseListRecursive(self, head):
            if head is None or head.next is None:
                return head

            tail = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return tail
