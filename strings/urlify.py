
'''
Full solution at https://devclass.io/urlify

Given a string with spaces, return the string, replacing each space with `%20`. Our input will contain additional empty chars to account for the chars needed to add when replacing an empty space with `%20`. Additional input is a number representing the length of the string without trailing spaces.

_Note_

- Strings are immutable in python so our input will be a list with every item containing a letter.

**Example 1**

`Input: ['h', 'e', 'y', ' ', 'y', 'o', 'u', ' ', ' '], 7`

`Output: ['h', 'e', 'y', '%','2', '0', 'y', 'o', 'u']`
'''


class NaiveSolution:
    def URLify(self, input, strLen):
        output = []
        for char in input:
            if char != ' ':
                output.append(char)
            else:
                output.append('%20')
        return output
