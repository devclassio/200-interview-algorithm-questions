## What is an Algorithm?

Before we write a ton of these it will be helpful to have a formal definition.

- An algorithm is a set of instructions on how to accomplish a specific task.
- An algorithmic problem defines the set of instances on which it works. For example some algos work on a `Array<int>` while others work on `Array<String>`

## What makes an algorithm good?

A good algorithm has 3 main features

- Correct -> This one is important. If our algorithm doesn't solve our problem we haven't done much have we? We need to show that every `valid` input to our algorithm maps to a correct result. In academia, proving the correctness of an algorithm can be a rigorous mathematical exercise. In this book, we'll skip these as we're aiming to develop intuition.
- Efficient -> The algorithm should minimize the amount of redundant work done! Besides being kind to our computer CPU this also translates into how long it will take the algorithm to resolve.
- Easy to read -> As a programmer this should always be the aim! Not only so that our co-workers won't grimace every time they see a pull request -- it's also for ourselves! We've all encounterd code we wrote months ago and didn't understand. Let's try and minimize these instances moving forward.

## Why is efficiency important?

I know what some of ya'll are thinking... Does efficiency still matter today? I can create amazing Tik Toks with AR filters, stream video games with friends all over the world in realtime and even mine bitcoin on my laptop (good luck with that one!). I'm sure any computer can handle my trivial code! Unfortunatley, this isn't true yet! We'll review a few seemingly innocent / common problems which have straighforward solutions which are so innefficient that they'd literally take `lifetimes` to resolve!!!
