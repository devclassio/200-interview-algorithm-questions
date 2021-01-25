'''
Full solution at https://devclass.io/palindrome-permutation

_Palindrome Definition_
a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

Given a string, write a function to check if the string is a palindrome, or if the letters can be rearranged to form a palindrome.

_Note_
When checking for a palindrome you can ignore empty spaces
'''


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        seen = {}
        for char in s:
            if char != " ":
                seen[char] = seen.get(char, 0) + 1
        oddCounter = 0
        for val in seen.values():
            if val % 2 == 1:
                oddCounter += 1
            if oddCounter > 1:
                return False
        return True
