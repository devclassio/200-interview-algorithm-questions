'''
Can't cache here! arr is too big! need to use this math trick :)
'''


class OmerSolution:
    '''
    Great example! to make this work with memoize i think arr must be of len n/2
    '''

    def myPow(self, x, n):
        self.cache = [None] * (abs(n) + 1)
        self.cache[0] = 1

        def helper(x, n):
            if self.cache[n]:
                return self.cache[n]
            if self.cache[n-1]:
                return x * self.cache[n-1]
            self.cache[n-1] = helper(x, n - 1)
            return x * self.cache[n - 1]

        return helper(x, n) if n > 0 else 1 / helper(x, -n)


class Solution:
    def myPow(self, x, n):
        def helper(x, n):
            if n == 0:
                return 1
            # compute
            if (n - 1) % 2 == 0:
                oneBefore = helper(x * x, int(n / 2))
            else:
                oneBefore = x * helper(x * x, int((n - 1) / 2))

            # solution
            return x * oneBefore

        if n < 0:
            x = 1 / x
            n = -n

        squared = x * x
        exp = n / 2 if n % 2 == 0 else (n - 1) / 2

        return helper(squared, exp) if n % 2 == 0 else x * helper(squared, exp)
