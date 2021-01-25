'''
Full solution at https://devclass.io/check-permutation

Given two strings, write a function to determine if the first string is a permutation of the second
'''


class SpaceSolution:
    def isPermutation(self, s1, s2):
        return sorted(s1) == sorted(s2)


class TimeSolution:
    def isPermutation(self, s1, s2):
        seen = {}
        for char in s1:
            seen[char] = seen.get(char, 0) + 1
        for char in s2:
            if char not in seen:
                return False
            char[seen] -= 1
            if char[seen] < 0:
                return False
        return True
