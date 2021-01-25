'''
Full solution at https://devclass.io/is-unique

Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

'''


class NaiveSolution:
    def isUnique(self, input):
        for idx1, char1 in enumerate(input):
            for idx2, char2 in enumerate(input):
                # make sure the duplicate char is not a sighting of the same char!
                if char1 == char2 and idx1 != idx2:
                    return False
        return True


class SpaceOptimizedSolution:
    def isUnique(self, input):
        seenChars = set()
        for char in input:
            if char in seenChars:
                return False
            else:
                seenChars.add(char)
        return True
