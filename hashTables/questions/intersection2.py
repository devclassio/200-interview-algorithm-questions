'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''


class SolutionOptimal(object):
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


class Solution:
    def intersect(self, nums1, nums2):
        occs1, occs2 = {}, {}
        intersection = list(set(nums1) & set(nums2))

        for num in nums1:
            if num not in intersection:
                continue
            if num in occs1:
                occs1[num] += 1
            else:
                occs1[num] = 1

        for num in nums2:
            if num not in intersection:
                continue
            if num in occs2:
                occs2[num] += 1
            else:
                occs2[num] = 1

        res = []
        print(occs1)
        print(occs2)
        for num in intersection:
            for i in range(min(occs1[num], occs2[num])):
                res.append(num)

        return res
