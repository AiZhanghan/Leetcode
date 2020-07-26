class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        
        Args:
            matrix: list[list[int]]
        """
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        
        row0_zero = False
        col0_zero = False

        for j in range(col):
            if matrix[0][j] == 0:
                row0_zero = True
                break
        
        for i in range(row):
            if matrix[i][0] == 0:
                col0_zero = True
                break
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if row0_zero:
            matrix[0] = [0] * col
        
        if col0_zero:
            for i in range(row):
                matrix[i][0] = 0


# class Solution:
#     def setZeroes(self, matrix):
#         """
#         Do not return anything, modify matrix in-place instead.
        
#         Args:
#             matrix: list[list[int]]
#         """
#         if not matrix:
#             return
#         m = len(matrix)
#         n = len(matrix[0])

#         row_mask = 0
#         col_mask = 0
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     row_mask |= 1 << i
#                     col_mask |= 1 << j
        
#         i = 0
#         while row_mask:
#             if row_mask & 1 == 1:
#                 matrix[i] = [0] * n
#             row_mask >>= 1
#             i += 1
        
#         j = 0
#         while col_mask:
#             if col_mask & 1 == 1:
#                 for i in range(m):
#                     matrix[i][j] = 0
#             col_mask >>= 1
#             j += 1
        
        