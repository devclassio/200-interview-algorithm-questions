'''
WIP permutations.
'''


def combos(s):

    if len(s) == 0:
        return []

    if len(s) == 1:
        return [s]

    if len(s) == 2:
        return [s, s[1] + s[0]]

    all = []
    for idx, l in enumerate(s):
        tmp = s[0]
        asL = list(s)
        asL[0] = l
        asL[idx] = tmp
        asL = str(asL)
        all.append([[asL[0]] + combos(asL[1:])])
    return all


def printCombos(o):
    all = combos(o)
    for s in all:
        print(s)


print("****** Test 0 *******")
printCombos("a")

print("****** Test 1 *******")
printCombos("ab")

print("****** Test 2 *******")
printCombos("abc")

print("****** Test 3 *******")
printCombos("abcd")
