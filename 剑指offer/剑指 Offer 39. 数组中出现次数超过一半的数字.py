class Solution:
    def majorityElement(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        votes = 0
        for num in nums:
            if votes == 0:
                res = num
            if num == res:
                votes += 1
            else:
                votes -= 1
        return res