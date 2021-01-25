'''
Full solution at https://devclass.io/string-compression

We're writing a string compression algorithm! Implement a method to perform basic compression using the counts of repeated characters.

**Example**

`Input: aabcccccaaa`
`Output: a2b1c5a3`

If the compressed string is not smaller than the original than return the original. You can assume all chars in the input are A-Z, a-z.
'''


class Solution:
    def stringCompress(self, s):
        compressed = []
        currentChar, streakCounter = s[0], 1
        for char in s[1:]:
            if char == currentChar:
                streakCounter += 1
            else:
                compressed.append(currentChar + str(streakCounter))
                currentChar, streakCounter = char, 1

        # append the last char
        compressed.append(currentChar + str(streakCounter))
        compressed = "".join(compressed)

        return compressed if len(compressed) < len(s) else s
