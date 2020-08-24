class Solution:
    def func(self, matrix, n):
        """
        Args:
            matrix: list[list[int]]
            n: int
        
        Return:
            int
        """
        self.res = 0
        self.dfs(matrix, 0, n, 0)
        return self.res

    def dfs(self, matrix, index, rest_n, path):
        """
        Args:
            matrix: list[list[int]]
            index: int
            rest_n: int
            path: int
        """
        if index == len(matrix) or rest_n <= 0:
            self.res = max(self.res, path)
            return
        
        self.dfs(matrix, index + 1, rest_n, path)
        for j in range(rest_n):
            self.dfs(matrix, index + 1, rest_n - j - 1, path + matrix[index][j])


if __name__ == "__main__":
    m, n = list(map(int, input().split()))
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))
    print(Solution().func(matrix, n))
