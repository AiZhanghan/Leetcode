class Solution:
    def exist(self, board, word):
        """
        回溯
        parameter:
            board: list[list[str]]
            word: str
        return: bool
        """
        self.board = board
        self.word = word
        # self.visited = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(0, i, j):
                    return True
        return False

    def dfs(self, index, row, col):
        """
        parameter:
            index: int, 接下来要找的char
            row: int, 当前所在行
            col: int, 当前所在行
        return: bool
        """
        if (not 0 <= row < len(self.board)) or \
            (not 0 <= col < len(self.board[0])) or \
            (self.board[row][col] != self.word[index]):
            return False
        
        if index == len(self.word) - 1:
            return True
        
        tmp = "/"
        tmp, self.board[row][col] = self.board[row][col], tmp
        if self.dfs(index+1, row+1, col) or \
            self.dfs(index+1, row, col+1) or \
            self.dfs(index+1, row-1, col) or \
            self.dfs(index+1, row, col-1):
            return True
        else:
            tmp, self.board[row][col] = self.board[row][col], tmp
            return False


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    print(Solution().exist(board, word))