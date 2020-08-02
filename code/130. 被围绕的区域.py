class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        
        Args:
            board: list[list[str]]
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        
        for j in range(n):
            self.dfs(board, 0, j)
            self.dfs(board, m - 1, j)
        
        for i in range(1, m - 1):
            self.dfs(board, i, 0)
            self.dfs(board, i, n - 1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
    
    def dfs(self, board, i, j):
        """
        Args:
            i: int
            j: int
        """
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or \
            board[i][j] == "X" or board[i][j] == "#":
            return
        board[i][j] = "#"
        self.dfs(board, i - 1, j)
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)
