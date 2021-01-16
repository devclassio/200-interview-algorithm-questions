'''
Input :
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

Output :
 Union : [0, 1, 2, 3, 4, 5, 6, 8]
 Intersection : [2, 4]
 Difference : [8, 0, 6]
 Symmetric difference : [0, 1, 3, 5, 6, 8]
In Python, below quick operands can be used for different operations.

| for union.
& for intersection.
– for difference
^ for symmetric difference

https://leetcode.com/problems/intersection-of-two-arrays/
'''


class Solution:
    def intersection(self, nums1, nums2):
        intersection = set([])
        for num in nums1:
            if num in nums2:
                intersection.add(num)
        return list(intersection)
