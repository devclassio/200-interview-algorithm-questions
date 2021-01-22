## Intro

Trees are super useful data structures. They are used commonly because they are very useful in modelling real world problems. Let's take a look at some examples.

## Browsers and the DOM

The browser is a staple of our day to day lives. To be clear - we're talking chrome, safari, firefox, opera etc. Everytime your browser displays data it's actually parsing an abstract data type -> specifically, the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) tree to figure out how to paint the page. For more on the inner workings of the browser [check this out](https://medium.com/jspoint/how-the-browser-renders-a-web-page-dom-cssom-and-rendering-df10531c9969#:~:text=When%20a%20web%20page%20is,the%20Render%2DTree%20from%20it.).

## Modelling Decision Making

The root represents a starting state. Every node has N dsicrete children which present a different decision. Reaching a leaf represents a final outcome.

## Machine Learning

Decision Tree based Learning actually forms a formidable area of data mining research. Numerous famous methods exist like bagging, boosting, and modifications thereof which work on trees. Such work is often used to generate a predictive model.

## Bioinformatics

A common problem in bioinformatics is to search huge databases to find matches for a given query string. Tries are a common occurrence there.

## Searchable

Sorted Trees, like sorted arrays are easily searchable which is another massive benefit that makes them so popular. In the coming chapters we'll understand how a sorted array and a binary search tree are closely related. You can easily convert one to the other! Making these connections are super cool b/c you start to understand how all of CS theory is intertwined. Most of the differences wind up in the abstractions we decide to use and how we want to lay out the data on disk. Admittedly, in the age of cloud computing data layout is less of a concern, but it's still useful to keep in mind.

## Data Compression

This is actually one of my favorite uses of trees! Compressio (think `zipping` files) is the art of representing data in its minimal form. There are a ton of algos for this, many tree based. Compressing data enables fast data transfer all over the world. With the explosion of big data and internet connected devices everywhere efficent data representation and compression is absolutely essential. We'll be checking some of these out in the coming chapters:

- Huffman coding
- Ziv Lempel encoding
- and more!

## Formal definitions

Define a node

```
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

```

- Each tree has a root node
- Every root has N >= 0 children
- Each child may have its own children

## Why you should learn them

We know they can be tricky. But whether you like it or not, trees are an absolute cornerstone of computer science. Get comfortable with them early! It will unblock so much future work for you and give you a strong base for understanding so many other algorithms / thought processes moving forward.

At the end of the day thinking in a non linear fashion is a new thing for most. Working on trees often has quite elegant recursive solutions, which is another unique approach for problem modeling / solving.

Like many things, I think this easily solvable with practice! Let's get started!!

## Explanation

https://stackoverflow.com/questions/7423401/whats-the-difference-between-the-data-structure-tree-and-graph
