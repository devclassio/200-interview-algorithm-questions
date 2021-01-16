'''
Intuition

Imagine you are writing a small compiler for your college project and one of the tasks (or say sub-tasks) for the compiler would be to detect if the parenthesis are in place or not.

The algorithm we will look at in this article can be then used to process all the parenthesis in the program your compiler is compiling and checking if all the parenthesis are in place. This makes checking if a given string of parenthesis is valid or not, an important programming problem.

The expressions that we will deal with in this problem can consist of three different type of parenthesis:

(),
{} and
[]
Before looking at how we can check if a given expression consisting of these parenthesis is valid or not, let us look at a simpler version of the problem that consists of just one type of parenthesis. So, the expressions we can encounter in this simplified version of the problem are e.g.


https://leetcode.com/problems/valid-parentheses/solution/
'''


class Solution:
    def __init__(self):
        self.stack = []

    def isValid(self, s):
        for i, el in enumerate(s):
            if el == "(" or el == "{" or el == "[":
                self.stack.append(el)
            elif el == ")" or el == "}" or el == "]":
                if len(self.stack) == 0:
                    return False
                lastEl = self.stack[-1]
                if el == ")" and lastEl != "(":
                    return False
                if el == "}" and lastEl != "{":
                    return False
                if el == "]" and lastEl != "[":
                    return False
                self.stack.pop()
        return len(self.stack) == 0


class Solution2(object):
    def isValid(self, s):
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''
