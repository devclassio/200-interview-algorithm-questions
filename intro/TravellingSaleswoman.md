# Travelling Saleswoman Problem

This problem is often hidden in plain sight! Let's state it semi-formally so we're all on the same page.

A saleswoman has `N` destinations she needs to travel to. However, travel is expensive and time is short! She'd like to know the optimal (shortest) cyclic path she can take which covers all `N` points!

## Simple enough?

This problem sounds innocent, but in fact is basically impossible for a significant `N`. You can try proving me wrong (and win a Turing prize in the process) but the only real solution here is to check all possible paths! So formally, we would have something like this:

```
def shortestPath(paths: List[PossiblePath]) -> PossiblePath:
    minDistance = float('inf')
    bestPath = None
    for path in paths:
        currentDistance = getTimeToTraverse(path)
        if currentDistance < minDistance:
            minDistance = currentDistance
            bestPath = path
    return bestPath
```

With `N` different locations there are `N!` different paths that can be taken! For a small `N!` this could work, but this becomes unscalable prettttty quickly. Let's take a look at how many different permutations (paths) exist for a given `N`.

n = 1 -> `1`
n = 2 -> `2`
n = 4 -> `24`
n = 10 -> `3628800`
n = 20 -> `2.432902e+18`
n = 10,000 -> lol

That escalated quickly! <MEME>

## Breakdown

So, the algorithm is correct! It's even easy to read! But it's definitley not efficient. This algorithm doesn't scale at all! We could have thousands of computers working simultaneously for `n=10,0000` and they'd never complete...

## Takeaway

We can't always find an algorithm that is

1. Efficient
2. Easy to read
3. Correct

In cases (like this!) where efficiency and correctness are tradeoffs we will often settle for a good heuristic. A good software engineer understands that done is often better than perfect. Especially when done happens at time == Infinity ;)

[Glossary] -> Heuristic is:

`A heuristic technique, or a heuristic, is any approach to problem solving or self-discovery that employs a practical method that is not guaranteed to be optimal, perfect, or rational, but is nevertheless sufficient for reaching an immediate, short-term goal or approximation`
