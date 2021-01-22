'''
Given two arrays, write a function to compute their intersection.

**Example 1**

`Input: nums1 = [1,2,2,1], nums2 = [2,2]`
`Output: [2]`

**Example 2**

`Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]`
`Output: [9,4]`

**Note**

Each element in the result must be unique.
The result can be in any order.
'''


class NaiveSolution:
    def intersection(self, nums1, nums2):
        intersection = set([])
        for num in nums1:
            if num in nums2:
                intersection.add(num)
        return list(intersection)


class OptimalSolution:

    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        p1, p2, res = 0, 0, []
        while p1 < len(nums1) and p2 < len(nums2):
            c1, c2 = nums1[p1], nums2[p2]
            if c1 == c2:
                res.append(c1)
                while p1 < len(nums1) and c1 == nums1[p1]:
                    p1 += 1
                while p2 < len(nums2) and c2 == nums2[p2]:
                    p2 += 1
            elif c1 > c2:
                p2 += 1
            else:
                p1 += 1
        return res
