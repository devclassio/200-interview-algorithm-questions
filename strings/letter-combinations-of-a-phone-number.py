'''
Full solution at https://devclass.io/letter-combinations-of-a-phone-number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters. Here is the mapping as a visial

mapping = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
'''


class RecursiveSolution:
    def letterCombinations(self, digits):
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        all_but_last = self.letterCombinations(
            digits[:-1])  # all elements except last
        last = list(mapping[digits[-1]])  # "abc" -> ['a', 'b', 'c']
        res = []
        for char in last:
            for expression in all_but_last:
                res.append(expression + char)
        return res


class BacktrackingSolution:
    def letterCombinations(self, digits):
         map_ = {
              '2': 'abc',
              '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
              }
        res = []

           def make_combinations(i, accumalated):
                if i == len(digits):
                    if len(accumalated) > 0:
                        res.append(''.join(accumalated))
                    return
                for char in map_[digits[i]]:
                    accumalated.append(char)
                    make_combinations(i+1, cur)
                    accumalated.pop()

            make_combinations(0, [])

            return res
