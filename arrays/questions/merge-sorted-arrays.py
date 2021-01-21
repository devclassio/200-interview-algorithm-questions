'''
## Problem 🤔

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

`Input:`

`nums1 = [1,2,3,0,0,0], m = 3`
`nums2 = [2,5,6], n = 3`

`Output: [1,2,2,3,5,6]`
'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        # else:
        #     nums1[:m] = nums1[:m]
