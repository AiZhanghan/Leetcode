class Solution:
    def grayCode(self, n):
        """
        Args:
            n: int
        
        Return:
            list[int]
        """
        res = [0]
        head = 1
        for _ in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] + head)
            head <<= 1
        return res