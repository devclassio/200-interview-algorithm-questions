class Solution:
    def climbStairs(self, n):
        if n < 3:
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
