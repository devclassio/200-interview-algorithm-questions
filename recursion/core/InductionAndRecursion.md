## Intro

`Too understand recursion you must understand recursion`

Getting comfortable with recursion is one of the most important things one can do as a programmer.

It has major practical benefits, as well as benefits for a technical interview.

## Why recursion can be tricky

As engineers and humans most of us are used to thinking linearly. The first concepts we learn as engineers are `while` and `for` loops. This is in line with the type of thinking we already know. Thinking of the elements of a list [0,1,2,3,4,...,n] one at a time is quite simple isn't it? On the other hand, thinking in a recursive manner is new for the majority of engineers and the first we are introduced to this type of thinking is through mathematical induction or when we learn recursion.

## Is this magic?

There are many videos and books out there with recommendations on understanding recursion. I'd divide the main camps into 2:

1. Following the stack and keeping track of what's happening in memory

2. "The magic approach" -> This approach means that once you have a base case and a recurrence relation that invokes the function itself you should be good to go!

I've tried both. I find that following the stack gets very messy quickly! There's often too much state to keep track of and this becomes unrealistic for any input which isn't close to the base case. On the other hand, it's programming and I think believing in the black magic of programming isn't the best approach. Ultimately, understanding that recursion is mathematical induction is what helped recursion click for me! Oh yeah, and a lot of practice ;)

## Mathematical induction === Recursion

I had studied mathematical induction during high school! Even back then it seemed like magic! It is an extremely powerful method for and is used heavily as a mathematical proof technique (https://en.wikipedia.org/wiki/Mathematical_induction). Recursion is simply the programmatic emobdiment of it!

Let's confirm this with a high level statement on both recursion and induction:

In both, we have a base case (usually n == 1) and a general case. The general case breaks down the input into a smaller subproblem, moving towards the base case! <LINK TO RECURSION ARTICLE BREAKDOWN>.

One of the quotes that always stuck with me is the following:

`Computer Scientists is a mathematician who only knows how to prove things by induction.`

This is true because the vast majority of algorithms we use in the day to day are either incremental or recurisve!

Which brings me back to my original point of the importance of recursion. It can be argued that by not knowing recursion you're problem solving tool kit is only 50% complete...

## Light at the end of the tunnel

One recursion "clicks" they're often very easy to code out. This is meant as a word of encouragement. I've spent countless hours fumbling over recursive solutions, attempting to understand `why` they work! Do not despair! Once recursion `clicks` these quickly become the funnest, easiest and most concise problems you can solve! Another benefit in this regard is that the code is often clean and short :)

## Recursive data structures
