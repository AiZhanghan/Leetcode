class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        Args:   
            matrix: list[list[int]]
        
        Return:
            bool
        """
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True
        

# class Solution:
#     def isToeplitzMatrix(self, matrix):
#         """
#         Args:   
#             matrix: list[list[int]]
        
#         Return:
#             bool
#         """
#         # 第一列
#         for i in range(len(matrix)):
#             if not self.check(matrix, i, 0):
#                 return False
#         # 第一行
#         for j in range(1, len(matrix[0])):
#             if not self.check(matrix, 0, j):
#                 return False
        
#         return True
    
#     def check(self, matrix, row, col):
#         """
#         Args:
#             matrix: list[list[int]]
#             row: int
#             col: int
        
#         Return:
#             bool
#         """
#         num = matrix[row][col]
#         while row < len(matrix) and col < len(matrix[0]):
#             if matrix[row][col] != num:
#                 return False
#             else:
#                 row += 1
#                 col += 1
#         return True