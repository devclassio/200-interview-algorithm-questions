## Aspiring Writer

Let's discuss a purely hypothetical situation. I am an aspiring writer who is trying to build his reputation by producing a larger body of work.

- My objective is to maximize my fame.
- Due to external dependencies I am offered certain projects throughout the year.
- I cannot commit to more than one project at a time (no simultaneous work)\* Projects can have different durations but all of them increase my fame by the same amount (identical utility)

## Objective

Input: List[{JobTitle: String, Start: Date, End: Date}]
Output: List[{JobTitle: String, Start: Date, End: Date}] s.t. fame is max
Or in other words, find the optimal schedule such that I maximize my fame for the coming year!

## Earliest Starting Jobs

Naive solution -> Let's always take the job that starts earliest!

This wont work :/

What if the first job starts January 1st but takes 12 months and I have many other shorter jobs that start afterwards?

[{"AlgoTeacher", "Jan", "December"}, {"AlgoTeacher 2", "Feb", "Feb"}, {"AlgoTeacher 3", "March", "March"}]

Formally:

```
def earlyJobs(writingGigs: List[{JobTitle: String, Start: Date, End: Date}]):
    fame = 0
    while len(writingGigs) > 0:
        fame = fame + getEarliestJobProfitAndDeleteOverlapping
    return fame
```

## Shortest Jobs

Maybe we should take the shortest jobs first?

```
def shortestJobs(writingGigs: List[{JobTitle: String, Start: Date, End: Date}]):
    fame = 0
    while len(writingGigs) > 0:
        fame = fame + getShortestJobProfitAndDeleteOverlapping
    return fame
```

This doesn't work! What if the shortest jobs always overlap with 2 others!

[{"AlgoTeacher", "Jan", "May"}, {"AlgoTeacher 2", "April", "June"}, {"AlgoTeacher 3", "June", "December"}]

## Search All Options

When all else fails, let's just check... everything?

So with N writing gigs that leaves us to check 2^n options.

When n = 1000 we again reach values which can't be computed by regular computers.

## Earliest Ending Jobs

```
def earliestEndingJobs(writingGigs: List[{JobTitle: String, Start: Date, End: Date}]):
    fame = 0
    while len(writingGigs) > 0:
        fame = fame + getEarliestEndingJobProfitAndDeleteOverlapping
    return fame
```

Or in python:

```
https://leetcode.com/problems/maximum-length-of-pair-chain/solution/
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        intervals = sorted(pairs, key=lambda v: v[1])
        chain = [intervals[0]]
        for interval in intervals[1:]:
            lastChain = chain[-1]
            s,e = interval[0], interval[1]
            if s > lastChain[1]:
                chain.append(interval)
        return len(chain)
```

Note: This explanation should be a video because it's a proof through negation...

## Takeaway

Reasonable looking algorithms can be dangerous because they can be wrong!
