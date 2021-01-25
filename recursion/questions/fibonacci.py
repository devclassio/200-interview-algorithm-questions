'''
Full solution at https://devclass.io/fibonacci

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

`F(0) = 0, F(1) = 1`

`F(N) = F(N - 1) + F(N - 2), for N > 1.`

Given N, calculate F(N).
'''


class Solution:
    def fib(self, N):
        if N == 0 or N == 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
