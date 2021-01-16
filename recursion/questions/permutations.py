'''
Generate permutations -> Compute the permutations of an array.
Write a program that takes as input an array of distinct integers
and generates all permuations of that array

[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
'''


def combos(s):

    if len(s) == 0:
        return []

    if len(s) == 1:
        return s

    if len(s) == 2:
        return [s, [s[1], s[0]]]

    all = []
    for i, pivot in enumerate(s):
        s[0], s[i] = s[i], s[0]
        for p in combos(s[1:]):
            all.append([s[0]] + p)

    return all


def printCombos(o):
    all = combos(o)
    for s in all:
        print(s)


print("**** Test 0 *****")
printCombos([])

print("**** Test 1 *****")
printCombos([1])

print("**** Test 2 *****")
printCombos([1, 2])

print("**** Test 3 *****")
printCombos([1, 2, 3])

print("**** Test 4 *****")
printCombos([1, 2, 3, 4])
