'''

Full write up here: https://devclass.io/generate-all-subsets-of-size-k/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.

**Example 1**
`Input: n = 5, k = 2`
`Output: [[1,2], [1,3], [1,4], [1,5], [2,3], [2,4], [2,5], [3,4], [3,5], [4,5]]`

**Example 2**
`Input: n = 4, k = 2`
`Output: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]`

**Example 3**
`Input: n = 1, k = 1`
`Output: [[1]]`
'''


class RecursiveSolution:
    def combine(self, n, k):
        def subsets(accumalated, index):
            if len(accumalated) == k:
                res.append(accumalated)
                return
            elif len(accumalated) > k:
                return

            for i in range(index, n+1):
                subsets(accumalated+[i], i+1)

        res = []
        subsets([], 1)
        return res


class BacktrackingSolution:
    def combine(self, n, k):
        def subsets(accumalated, index):
            if len(accumalated) == k:
                res.append(accumalated[:])
                return

            for i in range(index, n+1):
                accumalated.append(i)
                subsets(accumalated, i+1)
                accumalated.pop()

        res = []
        subsets([], 1)
        return res
