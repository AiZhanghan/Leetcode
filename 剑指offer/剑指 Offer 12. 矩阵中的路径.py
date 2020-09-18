class Solution:
    def exist(self, board, word):
        """
        Args:
            board: list[list[str]]
            word: str
        
        Return:
            bool
        """
        visited = [[False for _ in range(len(board[0]))] 
            for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, 0, word, visited):
                    return True
        return False
    
    def dfs(self, board, row, col, index, word, visited):
        """
        Args:
            board: list[list[str]]
            row: int
            col: int
            path: list[str]
            word: str
            visited: list[list[bool]]
        
        Return:
            bool
        """
        if index == len(word):
            return True
        if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1 \
            or visited[row][col] or board[row][col] != word[index]:
            return False
        
        visited[row][col] = True
        res = self.dfs(board, row + 1, col, index + 1, word, visited) \
            or self.dfs(board, row - 1, col, index + 1, word, visited) \
            or self.dfs(board, row, col + 1, index + 1, word, visited) \
            or self.dfs(board, row, col - 1, index + 1, word, visited)
        visited[row][col] = False

        return res


if __name__ == "__main__":
    board = [["a","b"]]
    word = "ba"
    print(Solution().exist(board, word))