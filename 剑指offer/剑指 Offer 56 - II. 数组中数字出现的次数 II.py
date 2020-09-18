class Solution:
    def singleNumber(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        res = 0
        for i in range(32):
            count = 0
            bit_mask = 1 << i
            for num in nums:
                if num & bit_mask != 0:
                    count += 1
            if count % 3 != 0:
                res |= bit_mask
        return res - 2 ** 32 if res > 2 ** 31 - 1 else res