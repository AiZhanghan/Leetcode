class Solution:
    def findComplement(self, num):
        """
        Args:
            num: int
        
        Return:
            int
        """
        temp = 1
        while temp < num:
            temp <<= 1
            temp += 1
        return temp ^ num