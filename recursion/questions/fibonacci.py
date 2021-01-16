class Solution:
    def climbStairs(self, n):
        if n < 3:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
