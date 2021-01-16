## Recurisve Data Structures

Learning to think recursively is being able to understand how a big problem is built
from smaller sub problems.

These types of constructs are actually around every single day. It's just a matter of perspective!

Let's look at popular data structures and CS problems. You may have thought of them until now in a more linear fashion. Here we will model them in a recurisve fashion.

## Trees

- Delete a leaf of a tree -> What do you get? A smaller tree!
- Delete the root of a tree -> What do you get? 2 trees!

## Graphs

**Note, tress and graphs behave the same, a tree is simply a directed graph**
Delete a node from a graph -> What do you get? A smaller graph
Delete an edge from a graph -> What do you get? 2 graphs!

## Strings

Delete a char from a string -> Wdyg? A smaller string!

## Subsets

Every subset of the elements {1,...,n} contains all the subsets of {1,...,n-1}. For each of the subsets of {1,..,n-1} we decide whether or not to append n.
Subsets are recursive data structures!

## Conclusion

This goes on and on! The purpose of this exercise is to understand

1. Recursiveness is a fundamental building block of CS - we can model all of our data structures as recursive objects.
2. Recurisveness is a matter of outlook or how you choose to model a problem. Any thing that can be done with iteration can also be represented or coded recursively.
