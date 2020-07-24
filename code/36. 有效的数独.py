class Solution:
    def isValidSudoku(self, board):
        """
        Args:
            board: list[list[str]]

        Return:
            bool
        """
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    if rows[i][num] > 1 or cols[j][num] > 1 \
                        or boxes[box_index][num] > 1:
                        return False
        return True
        

# class Solution:
#     def isValidSudoku(self, board):
#         """
#         Args:
#             board: list[list[str]]

#         Return:
#             bool
#         """
#         for i in range(9):
#             visited = set()
#             for j in range(9):
#                 if board[i][j] == ".":
#                     continue
#                 elif board[i][j] in visited:
#                     return False
#                 else:
#                     visited.add(board[i][j])

#         for j in range(9):
#             visited = set()
#             for i in range(9):
#                 if board[i][j] == ".":
#                     continue
#                 elif board[i][j] in visited:
#                     return False
#                 else:
#                     visited.add(board[i][j])
        
#         blocks = [
#             [0, 0], [0, 3], [0, 6],
#             [3, 0], [3, 3], [3, 6],
#             [6, 0], [6, 3], [6, 6]
#         ]
#         for x, y in blocks:
#             visited = set()
#             for i in range(3):
#                 for j in range(3):
#                     if board[x + i][y + j] == ".":
#                         continue
#                     elif board[x + i][y + j] in visited:
#                         return False
#                     else:
#                         visited.add(board[x + i][y + j])
    
#         return True


# if __name__ == "__main__":
#     board = [
#         ["5","3",".",".","7",".",".",".","."],
#         ["6",".",".","1","9","5",".",".","."],
#         [".","9","8",".",".",".",".","6","."],
#         ["8",".",".",".","6",".",".",".","3"],
#         ["4",".",".","8",".","3",".",".","1"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".","6",".",".",".",".","2","8","."],
#         [".",".",".","4","1","9",".",".","5"],
#         [".",".",".",".","8",".",".","7","9"]
#     ]
#     print(Solution().isValidSudoku(board))