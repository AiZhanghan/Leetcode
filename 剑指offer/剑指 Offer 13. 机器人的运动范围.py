class Solution:
    def movingCount(self, m, n, k):
        """
        Args:
            m: int
            n: int
            k: int
        
        Return:
            int
        """
        self.m = m
        self.n = n
        self.k = k
        self.res = 0
        self.visited = [[False for _ in range(n)] for _ in range(m)]

        self.dfs(0, 0)
        return self.res
    
    def dfs(self, i, j):
        """
        Args:
            i: int
            j: int
        """
        if i >= self.m or j >= self.n or self.visited[i][j] \
            or not self.is_valid(i, j):
            return
        
        self.visited[i][j] = True
        self.res += 1

        self.dfs(i + 1, j)
        self.dfs(i, j + 1)
    
    def is_valid(self, i, j):
        """
        Args:   
            i: int
            j: int
        
        Return:
            bool
        """
        return self.digit_sum(i) + self.digit_sum(j) <= self.k
    
    def digit_sum(self, num):
        """
        Args:
            num: int
        
        Return:
            int
        """
        res = 0
        while num:
            res += num % 10
            num //= 10
        return res
