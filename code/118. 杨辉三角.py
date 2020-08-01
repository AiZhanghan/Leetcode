class Solution:
    def generate(self, numRows):
        """
        Args:
            numRows: int
        
        Return:
            list[list[int]]
        """
        res = []
        for i in range(numRows):
            temp = [1 for _ in range(i + 1)]
            for j in range(1, len(temp) - 1):
                temp[j] = res[-1][j - 1] + res[-1][j]
            res.append(temp[:])

        return res