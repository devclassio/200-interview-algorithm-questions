class Solution:
    def subsets(self, nums):
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [[], nums]

        subs = [[], nums]
        for i, el in enumerate(nums):
            newSubs = self.subsets(nums[:i] + nums[i+1:])
            for s in newSubs:
                if s not in subs:
                    subs = subs + [s]

        return subs
