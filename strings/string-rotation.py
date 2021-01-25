'''
Full solution at https://devclass.io/string-rotation

Assume you have a method `isSubstring` which checks if one word is a substring of another. Given two strings, `s1` and `s2`, write code to check if `s2` is a rotation of `s1`, using only one call to `isSubstring`.

**Example**

`Input: s1 = waterbottle, s2 = erbottlewat`

`Output: true`
'''


class Solution:
    def isSubstring(self, s1, s2):
        pass

    def isRotation(self, s1, s2):
        return self.isSubstring(s1, s2 + s2)
