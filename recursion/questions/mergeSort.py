'''
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2944

Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

'''


class Solution:
    def mergeArrays(self, l1, l2):
        i, j = 0, 0
        merged = []

        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                merged.append(l1[i])
                i = i + 1
            else:
                merged.append(l2[j])
                j = j + 1

        if i < len(l1):
            merged = merged + l1[i:]
        if j < len(l2):
            merged = merged + l2[j:]
        return merged

    def sortArray(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums
        if len(nums) == 2:
            return nums if nums[0] <= nums[1] else [nums[1], nums[0]]
        middle = int(len(nums) / 2)
        l = nums[0:middle]
        r = nums[middle:]
        return self.mergeArrays(self.sortArray(l), self.sortArray(r))
