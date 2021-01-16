# Recursion Building Blocks

On a high level we know that a working recurisve function has:

1. A base case
2. Calls itself (hence the recursion!)

Let's formalize the second step. This is called the recurrence relation. In other words, the relationship between the subprolem `f(m), s.t. m << n` and `f(n)`.

Let's look remember the fibonacci or climbing stair problem (they're the same!)

The recurrence relation here would be `f(n) = f(n-1) + f(n-2)`.

So this is great! Because once we've defined a base case, we can simply get the solution to a recursive problem by returning its recurrence relation!

So all together:

To solve a recursive problem we need to

1. Find the recurrence relation between the subproblems and our problem.
2. Have a working base case!

## Why is this important?

For anyone who has practiced recursion, this is probably not new. However, giving these steps / mechanics correct naming, will allow us to easily explain and reason about our solution moving forward.

## Another sanity check

Always double check that your base case and recurrence relation return the same type, and that is the expected type!
