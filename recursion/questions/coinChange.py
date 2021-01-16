'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
'''


class SolutionTLE:
    '''
    How many ways? 1 + recursive
    Best way? DP
    '''

    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        dp = [float('inf')] * (amount + 1)

        def helper(coins, amount, used):
            if amount == 0:
                dp[amount] = min(dp[amount], used)
                return dp[amount]
            if amount < 0:
                return float('inf')
            if not coins:
                return dp[amount]

            newTarget = amount - coins[-1]
            removedCoin = coins[:len(coins) - 1]

            use = helper(coins, newTarget, used + 1)
            dontUse = helper(removedCoin, amount, used)
            dp[amount] = min(dp[amount], dontUse, use)

            return dp[amount]

        helper(coins, amount, 0)
        return - 1 if dp[-1] == float('inf') else dp[-1]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
