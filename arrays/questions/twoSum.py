'''
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''


class Solution:
    '''
    O(n), O(n)
    '''

    def twoSum(self, nums, target):
        current = target

        # Init dictionary
        yDict = {}
        for i, num in enumerate(nums):
            if num not in yDict:
                yDict[num] = [(target - num, i)]
            else:
                yDict[num].append((target - num, i))

        for i, num in enumerate(nums):
            compliment, index = yDict[num][0]
            if compliment in yDict:
                if compliment != num:
                    _, jIndex = yDict[compliment][0]
                    return [index, jIndex]
                elif len(yDict[compliment]) > 1:
                    _, jIndex = yDict[compliment][1]
                    return [index, jIndex]
        return []

    def twoSumPretty(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i