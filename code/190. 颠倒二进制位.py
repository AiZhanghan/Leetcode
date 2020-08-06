class Solution:
    def reverseBits(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        res = 0
        count = 32
        while count:
            res += n & 1
            res <<= 1
            n >>= 1
            count -= 1
        return res