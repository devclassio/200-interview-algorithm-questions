# Intro

An array is a contiguously-allocated data structure. Since arrays are fixed sized data records we can efficiently find each element by its index.

## Strengths

- Constant-time access - O(1), the index of each element maps to a specific address in memory.
- Space efficient - O(n), arrays are pure data, so no space wasted.
- Memory locality - Arrays exhibit excellent memory locality and utilizes high speed memory cache. (Link here to article)

## Weaknesses

- In statically typed languages, we cannot dynamically change the sizing of an array. Therefore we need to know how much memory is required ahead of time.
