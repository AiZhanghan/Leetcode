class Solution:
    def singleNumbers(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            list[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        
        mask = xor & (-xor)

        a = 0
        b = 0
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        
        return [a, b]
