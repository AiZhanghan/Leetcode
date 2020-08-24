class Solution:
    def constructArray(self, n, k):
        """
        Args:
            n: int
            k: int
        
        Return:
            list[int]
        """
        res = [0 for _ in range(n)]
        num_k = k + 1
        num_temp = 1
        for i in range(0, k + 1, 2):
            res[i] = num_temp
            num_temp += 1
        for i in range(1, k + 1, 2):
            res[i] = num_k
            num_k -= 1
        for i in range(k + 1, n):
            res[i] = i + 1
        return res
