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
        self.res = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        self.dfs(m, n, k, 0, 0, visited)
        return self.res
    
    def dfs(self, m, n, k, row, col, visited):
        """
        Args:
            m: int
            n: int
            k: int
            row: int
            col: int
            visited: list[bool]
        """
        if row < 0 or row >= m or col < 0 or col >= n \
            or visited[row][col] or not self.valid(row, col, k):
            return
        
        visited[row][col] = True
        self.res += 1
        self.dfs(m, n, k, row + 1, col, visited)
        self.dfs(m, n, k, row - 1, col, visited)
        self.dfs(m, n, k, row, col + 1, visited)
        self.dfs(m, n, k, row, col - 1, visited)
        
    def valid(self, row, col, k):
        """
        Args:
            row: int
            col: int
            k: int
        
        Return:
            bool
        """
        digit_sum = 0
        while row:
            digit_sum += row % 10
            row //= 10
        while col:
            digit_sum += col % 10
            col //= 10
        return digit_sum <= k