class Solution:
    def paintingPlan(self, n, k):
        """
        Args:
            n: int
            k: int
        
        Return:
            int
        """
        if k == 0 or k == n * n:
            return 1
        res = 0
        for i in range(n):
            for j in range(n):
                if n * (i + j) - (i * j) == k:
                    res += self.combination(n, i) * self.combination(n, j)
        return res

    def combination(self, n, m):
        """
        组合

        Args:
            n: int
            m: int, n >= m
        
        Return:
            int
        """
        res = 1
        for i in range(n, n - m, -1):
            res *= i
        for i in range(1, m + 1):
            res /= i
        return int(res)


if __name__ == "__main__":
    n = 2
    k = 4
    print(Solution().paintingPlan(n, k))