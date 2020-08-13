class Solution:
    def rob(self, nums):
        """
        Args:
            list[int]
        
        Return:
            int
        """
        return max(self.helper(nums[1:]), self.helper(nums[:-1])) \
            if len(nums) != 1 else nums[0]

    def helper(self, nums):
        """
        Args:
            list[int]
        
        Return:
            int
        """
        pre_pre = 0
        pre = 0
        for num in nums:
            cur = max(pre, pre_pre + num)

            pre_pre = pre
            pre = cur
        return pre