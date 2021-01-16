'''
https://leetcode.com/problems/maximum-length-of-pair-chain/solution/

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000]
'''


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        intervals = sorted(pairs, key=lambda v: v[1])
        lastInterval = intervals.pop(0)
        chainLen = 1
        for interval in intervals:
            s, e = interval[0], interval[1]
            if s > lastInterval[1]:
                lastInterval = interval
                chainLen = chainLen + 1
        return chainLen
