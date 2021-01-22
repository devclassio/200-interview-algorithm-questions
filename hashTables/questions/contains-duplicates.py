'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

**Example 1**

`Input: [1,2,3,1]`
`Output: true`

**Example 2**

`Input: [1,2,3,4]`
`Output: false`

**Example 3**

`Input: [1,1,1,3,3,4,3,2,4,2]`
`Output: true`
'''


class SolutionOptimalRuntime:
    '''
    Time, Space: O(n)
    '''

    def containsDuplicate(self, nums):
        self.seen = {}
        for num in nums:
            if num in self.seen:
                return True
            self.seen[num] = True
        return False


class SolutionOptimalSpace:
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
