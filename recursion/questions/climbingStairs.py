'''
Full write up is here! https://devclass.io/climbing-stairs

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example 1**

`Input: n = 2`

`Output: 2`

_Explanation_

There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps

'''


class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class SolutionMemoize:
    def climbStairs(self, n):
        if n < 3:
            return n

        memo = [-1] * n
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2

        def climbHelper(n):
            if n <= 2:
                return memo[n]
            for i in range(3, n):
                memo[i] = memo[i-1] + memo[i-2]
            return memo[n-1] + memo[n-2]

        return climbHelper(n)
