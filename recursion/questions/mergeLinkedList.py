'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None or l2 is None:
            return l2 or l1

        new = ListNode(None, None)
        if l1.val < l2.val:
            new = l1
            l1 = l1.next
        else:
            new = l2
            l2 = l2.next
        new.next = self.mergeTwoLists(l1, l2)
        return new
