class Solution:
    def printNumbers(self, n):
        """
        Args:
            n: int
        
        Return:
            list[int]
        """
        res = [x for x in range(1, 10 ** n)]
        return res