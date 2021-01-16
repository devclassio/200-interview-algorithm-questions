class SolutionRecursive:
    '''
    Given a linked list, swap every two adjacent nodes and return its head.

    You may not modify the values in the list's nodes. Only nodes itself may be changed.

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
