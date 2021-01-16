class Solution:

    def add(self, arr):
        return arr.pop() if len(arr) == 1 else arr.pop() + self.add(arr)
