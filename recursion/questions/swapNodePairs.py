'''
Discuss divide and conquer here!

https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1681/
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
'''


class Solution:
    '''
    1->2->3->4

    2->1->4->3
    '''

    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        # next pointers
        newHead = head.next

        # swap nodes
        newHead.next, head.next = head, newHead.next

        # recursive step
        newHead.next.next = self.swapPairs(newHead.next.next)

        return newHead
