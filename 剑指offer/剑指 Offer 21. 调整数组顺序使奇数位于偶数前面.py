class Solution:
    def exchange(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            list[int]
        """
        # [0, i) odd
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums