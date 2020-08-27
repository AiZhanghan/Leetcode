from collections import Counter


class Solution:
    def findLHS(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        counter = Counter(nums)
        res = 0
        for key in counter:
            if key + 1 in counter:
                res = max(res, counter[key] + counter[key + 1])
        return res