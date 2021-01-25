'''
Full solution at https://devclass.io/one-away

There are 3 types of edits that can be performed on strings:

1. insert a character
2. remove a character
3. replace a character

Given 2 strings, write a function to check if they are 1 (or 0) edits away.
'''


class Solution:
    def isOneEditAway(self, s1, s2):
        if abs(len(s1) - len(s2)) > 1:
            return False
        p1, p2, edits = 0, 0, 0
        while p1 < len(s1) and p1 < len(s2):
            # same length, this is faking a char replacement
            if s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
            else:
                edits += 1
                if edits > 1:
                    return False
                if len(s1) == len(s2):
                    p1 += 1
                    p2 += 1
                elif len(s2) > len(s1):
                    # s2 is longer. our edit here would be deletion of a character
                    p2 += 1
                else:
                    # s1 is longer. our edit here would be deletion of a character
                    p1 += 1
        return True
