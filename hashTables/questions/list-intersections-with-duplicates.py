'''
Given two arrays, write a function to compute their intersection.

**Example 1**

`Input: nums1 = [1,2,2,1], nums2 = [2,2]`
`Output: [2,2]`

**Example 2**

`Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]`
`Output: [4,9]`

**Note**

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

'''


class Solution(object):
    def intersect(self, nums1, nums2):

        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res
