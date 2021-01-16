'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.

https://leetcode.com/problems/first-unique-character-in-a-string/
'''


class Solution:
    def firstUniqChar(self, s):
        occs = {}
        length = len(s)
        for i in range(length):
            if s[i] in occs:
                occs[s[i]] += 1
            else:
                occs[s[i]] = 0

        for i in range(length):
            if occs[s[i]] == 0:
                return i
        return -1
