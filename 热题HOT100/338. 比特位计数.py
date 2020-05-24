class Solution:
    def countBits(self, num):
        """
        Args:
            num: int
        
        Return:
            list[int]
        """
        res = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            if i % 2 == 0:
                res[i] = res[i // 2]
            else:
                res[i] = res[i - 1] + 1
        return res