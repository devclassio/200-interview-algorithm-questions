## Arrays

Arrays are data structures of fixed size such that each element can be found by its index with O(1) look up time. They can be found on disk (RAM for the purpose of our discussions) as continuous blocks of memory.

## Memory allocation is a thing

In many languages, like Python we don't deal directly with memory allocation. When we declare a list, as programmers it seems like we can seemingly append forever. Alas, that isn't the case. All this nice high level programming converges to bits and bytes.

## Dynamic Arrays

Dynamic arrays are nice because they give us automatic resizing for free when needed. These are the default lists / arrays in JS / Python and many other programming languages.

## How Dynamic Arrays work

Dynamic arrays allocate a predetermined chunk of memory for every array declaration.
If more memory is needed, behind the scenes a new memory block is allocated, this time twice as large! In these cases, all the elements in the original array will be copied over into the new larger array. Copying each element takes O(n). That's the "downside" of dynamic arrays. Some append actions can take O(n)!
