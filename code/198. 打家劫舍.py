class Solution:
    def rob(self, nums):
        """DP
        
        Args:
            nums: list[int]
        
        Return；
            int
        """
        pre_pre = 0
        pre = 0
        for num in nums:
            cur = max(pre, pre_pre + num)
            
            pre_pre = pre
            pre = cur
        return pre
