class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        
        Args:
            board: list[list[int]]
        """
        if not board:
            return
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                state = 0
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >= 0 and nx < len(board) \
                        and ny >= 0 and ny < len(board[0]):
                        state += (board[nx][ny] & 1)
                if board[i][j] == 1:
                    if state == 2 or state == 3:
                        board[i][j] |= 2
                else:
                    if state == 3:
                        board[i][j] |= 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1
