class Solution:
    def twoSum(self, n):
        """
        Args:
            n: int
        
        Return:
            list[float]
        """
        dp = [0 for _ in range(70)]
        for i in range(1, 7):
            dp[i] = 1
        for i in range(2, n + 1):
            for j in range(6 * i, i - 1, -1):
                dp[j] = 0
                for cur in range(1, 7):
                    if j - cur < i - 1:
                        break
                    dp[j] += dp[j - cur]
        all = pow(6, n)
        res = []
        for i in range(n, 6 * n + 1):
            res.append(dp[i] / all)
        return res