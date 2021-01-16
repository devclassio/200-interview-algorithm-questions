'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
'''


class NaiveSolution:
    def maximumProduct(self, nums):
        smallestIndexes = []
        largestIndexes = []

        # Find smallest and largest
        smallest, largest = float('inf'), -float('inf')
        smallestIndexes.append(-1)
        largestIndexes.append(-1)
        for i, num in enumerate(nums):
            if num < smallest:
                smallest = num
                smallestIndexes.pop()
                smallestIndexes.append(i)
            if num > largest:
                largest = num
                largestIndexes.pop()
                largestIndexes.append(i)

        # Find second smallest and largest
        sSmallest, sLargest = float('inf'), -float('inf')
        smallestIndexes.append(-1)
        largestIndexes.append(-1)
        for i, num in enumerate(nums):
            if num < sSmallest and i not in smallestIndexes:
                sSmallest = num
                smallestIndexes.pop()
                smallestIndexes.append(i)
            if num > sLargest and i not in largestIndexes:
                sLargest = num
                largestIndexes.pop()
                largestIndexes.append(i)

        # Two prod
        smallestProd = sSmallest * smallest
        largestProd = sLargest * largest

        # Three prod
        threeProdS, threeProdL = -float('inf'), -float('inf')
        for i, n in enumerate(nums):
            if i not in smallestIndexes and n * smallestProd > threeProdS:
                threeProdS = n * smallestProd
            if i not in largestIndexes and n * largestProd > threeProdL:
                threeProdL = n * largestProd

        return max(threeProdS, threeProdL)

        '''
        public class Solution {
    public int maximumProduct(int[] nums) {
        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE, max3 = Integer.MIN_VALUE;
        for (int n: nums) {
            if (n <= min1) {
                min2 = min1;
                min1 = n;
            } else if (n <= min2) {     // n lies between min1 and min2
                min2 = n;
            }
            if (n >= max1) {            // n is greater than max1, max2 and max3
                max3 = max2;
                max2 = max1;
                max1 = n;
            } else if (n >= max2) {     // n lies betweeen max1 and max2
                max3 = max2;
                max2 = n;
            } else if (n >= max3) {     // n lies betwen max2 and max3
                max3 = n;
            }
        }
        return Math.max(min1 * min2 * max1, max1 * max2 * max3);
    }
}
        '''
