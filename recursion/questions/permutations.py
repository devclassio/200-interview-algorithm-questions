'''
Full write-up: https://devclass.io/generate-permutations
Generate permutations -> Compute the permutations of an array.
Write a program that takes as input an array of distinct integers
and generates all permuations of that array

[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
'''


class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        if len(nums) == 2:
            return [nums, [nums[1], nums[0]]]

        all = []
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
            for p in self.permute(nums[1:]):
                all.append([nums[0]] + p)

        return all


class SolutionPrettified(object):
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for permutation in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + permutation)
        return res
