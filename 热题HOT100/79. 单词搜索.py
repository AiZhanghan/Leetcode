from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """DFS"""
        self.board = board
        self.word = word
        self.visited = [[False for _ in range(len(board[0]))] 
                       for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, 0):
                    return True
        return False
    
    def dfs(self, i: int, j: int, index: int) -> bool:
        if index == len(self.word):
            return True
        if i < 0 or i >= len(self.board) \
            or j < 0 or j >= len(self.board[0]) \
            or self.visited[i][j] \
            or self.board[i][j] != self.word[index]:
            return False
        
        self.visited[i][j] = True
        res = self.dfs(i + 1, j, index + 1) \
            or self.dfs(i - 1, j, index + 1) \
            or self.dfs(i, j + 1, index + 1) \
            or self.dfs(i, j - 1, index + 1)
        self.visited[i][j] = False
        return res