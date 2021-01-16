## Duplicate Calculation in Recursion

Recursion is often an intuitive and powerful way to implement an algorithm. However, it might bring some undesired penalty to the performance, e.g. duplicate calculations, if we do not use it wisely.

In this article we will look closer into the duplicate calculations problem that could happen with recursion. We will then propose a common technique called memoization that can be used to avoid this problem.

To demonstrate another problem with duplicate calculations, let's look at an example that most people might be familiar with, the Fibonacci number. If we define the function F(n) to represent the Fibonacci number at the index of n, then you can derive the following recurrence relation:

## Memoization Example

F(n) = F(n - 1) + F(n - 2)
with the base cases:

F(0) = 0, F(1) = 1
Given the definition of a Fibonacci number, one can implement the function as follows:

def fibonacci(n):
"""
:type n: int
:rtype: int
"""
if n < 2:
return n
else:
return fibonacci(n-1) + fibonacci(n-2)

Now, if you would like to know the number of F(4), you can apply and extend the above formulas as follows:

F(4) = F(3) + F(2) = (F(2) + F(1)) + F(2)
As you can see, in order to obtain the result for F(4), we would need to calculate the number F(2) twice following the above deduction: the first time in the first extension of F(4) and the second time for the intermediate result F(3).

## Memoization

To eliminate the duplicate calculation in the above case, as many of you would have figured out, one of the ideas would be to store the intermediate results in the cache so that we could reuse them later without re-calculation.

This idea is also known as memoization, which is a technique that is frequently used together with recursion.

Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. (Source: wikipedia)

Back to our Fibonacci function F(n). We could use a hash table to keep track of the result of each F(n) with n as the key. The hash table serves as a cache that saves us from duplicate calculations. The memoization technique is a good example that demonstrates how one can reduce compute time in exchange for some additional space.

For the sake of comparison, we provide the implementation of Fibonacci number solution with memoization below.

As an exercise, you could try to make memoization more general and non-intrusive, i.e. applying memoization without changing the original function. (Hint: one can refer to a design pattern called decorator).

def fib(self, N):
"""
:type N: int
:rtype: int
"""
cache = {}
def recur_fib(N):
if N in cache:
return cache[N]

        if N < 2:
            result = N
        else:
            result = recur_fib(N-1) + recur_fib(N-2)

        # put result in cache for later reference.
        cache[N] = result
        return result

    return recur_fib(N)
