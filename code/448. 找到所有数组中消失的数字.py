class Solution:
    def findDisappearedNumbers(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            list[int]
        """
        for num in nums:
            new_index = abs(num) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)
            
        return res