class Solution:
    def group_number(self, matrix):
        """
        Args:
            matrix: list[list[int]]
        
        Return:
            int
        """
        if not matrix:
            return 0
        self.matrix = matrxi
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if matrix[i][j] == 1 and not self.visited[i][j]:
                    self.dfs(i, j)
                    res += 1
        return res
    
    def dfs(self, i, j):
        """
        Args:
            i: int
            j: int
        """
        if i < 0 or i >= self.m or j < 0 or j >= self.n \
            or self.matrix[i][j] != 1 or self.visited[i][j]:
            return
        self.visited[i][j] = True
        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)
