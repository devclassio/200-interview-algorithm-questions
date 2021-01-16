'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''


class Solution:
    def reverseString(self, s):
        middle = len(s) / 2

        def reverseHelper(s, index):
            if index >= middle:
                return
            end = len(s) - 1 - index
            s[index], s[end] = s[end], s[index]
            reverseHelper(s, index + 1)
        reverseHelper(s, 0)
