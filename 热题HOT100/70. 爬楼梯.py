class Solution:
    def climbStairs(self, n: int) -> int:
        """DP"""
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a