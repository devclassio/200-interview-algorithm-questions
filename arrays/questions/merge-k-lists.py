'''
## Problem 🤔

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example 1**

`Input: lists = [[1,4,5],[1,3,4],[2,6]]`
`Output: [1,1,2,3,4,4,5,6]`
_Explanation_
The linked-lists are:

```
[
1->4->5,
1->3->4,
2->6
]
```

merging them into one sorted list:

```
1->1->2->3->4->4->5->6
```

**Example 2**

`Input: lists = []`
`Output: []`

**Example 3**
`Input: lists = [[]]`
`Output: []`

**Note**

- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length won't exceed 10^4
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class NaiveSolution(object):
    def mergeKLists(self, lists):
        vals = []
        cur = ListNode(None)
        dummy_node = cur
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        for n in sorted(vals):
            cur.next = ListNode(n)
            cur = cur.next
        return dummy_node.next


class Solution:
    def mergeKLists(self, lists):
        heap = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(heap)
        cur = ListNode(None)
        dummy_node = cur
        while heap:
            val, idx = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
        return dummy_node.next
