class Solution:
    def singleNumbers(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            list[int]
        """
        k = 0
        for num in nums:
            k ^= num
        
        mask = 1
        while k & mask == 0:
            mask <<= 1
        
        a = 0
        b = 0
        for num in nums:
            if num & mask == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]
        