class Solution:
    def fib(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        if n < 2:
            return n
        pre_pre = 0
        pre = 1
        for _ in range(2, n + 1):
            cur = pre + pre_pre
            pre_pre = pre
            pre = cur
        return pre % 1000000007