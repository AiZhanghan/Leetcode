class Solution:
    def twoSum(self, nums, target):
        """
        Args:
            nums: list[int]
            target: int
        
        Return:
            list[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dic:
                return [dic[complement], i]
            dic[num] = i