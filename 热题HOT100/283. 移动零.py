class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Args:
            nums: list[int]
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if p != i:
                    nums[i], nums[p] = nums[p], nums[i]
                p += 1
        