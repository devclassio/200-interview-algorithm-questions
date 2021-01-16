## Recursion Technique: Divide and Conquer

Technically, all recursive solutions are divide and conquer because that's the base of mathematical induction :)

## base case

the case where one can compute the answer directly without any further recursion calls. Sometimes, the base cases are also called bottom cases, since they are often the cases where the problem has been reduced to the minimal scale, i.e. the bottom, if we consider that dividing the problem into subproblems is in a top-down manner.

## recurrence relation:

the relationship between the result of a problem and the result of its subproblems.

As discussed earlier, we need to ensure that every we invoke our recurisve function
we are getting closer to the base case! Otherwise, our function will never resolve itself, thus causing a maxmimum stack exception.

A great example of this is writing a recursive function to sum items in array.

```
def add(arr: List[int]) -> int:
    if len(arr) == 1:
        return arr.pop()
    return arr.pop() + add(arr)
```

Our base case is simple -> if our array has only 1 item the sum of the array is just
that item.

How does divide and conquer come into play?

We know how to handle the case of 1 element! Perfect!

So let's always pop off the last item, thus advancing our array to its base case!

## Tip:

Like I mentioned earlier -> The easiest way to think about recursion is having a working base case and confirming that the output of your recursive function matches the way in which it is being called!

So in `add`:

- my base case returns an int
- my recursive function call (last line of func) returns the summation of 2 ints!

## Divide and Conquer Template

Divide and conquer (D&C) is one of the most important paradigms in algorithm design and is widely used.

A divide-and-conquer algorithm works by recursively breaking the problem down into two or more subproblems of the same or related type, until these subproblems become simple enough to be solved directly [1]. Then one combines the results of subproblems to form the final solution.

As you can see, divide-and-conquer algorithm is naturally implemented in the form of recursion. Another subtle difference that tells a divide-and-conquer algorithm apart from other recursive algorithms is that we break the problem down into two or more subproblems in the divide-and-conquer algorithm, rather than a single smaller subproblem. The latter recursive algorithm sometimes is called decrease and conquer instead, such as Binary Search.

There are in general three steps that one can follow in order to solve the problem in a divide-and-conquer manner.

1. Divide. Divide the problem S into a set of subproblems:
2. Conquer. Solve each subproblem recursively.
3. Combine. Combine the results of each subproblem.

Examples: Merge sort, Quick sort
